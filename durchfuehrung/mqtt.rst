.. _ref-deye-mqtt:

###################################
Deye Wechselrichter MQTT Einbindung
###################################

Das `Github Projekt deye-inverter-mqtt <https://github.com/kbialek/deye-inverter-mqtt>`_ kann der Deye Wechselrichter ausgelesen werden und an einen MQTT Server zur weiteren Verteilung übergeben werden. Eine Anleitung zur Installation und Konfiguration ist auf der Github-Seite zu finden.


Konfiguration
=============

In der ``config.env`` wird im Wesentlichen die IP-Adresse und der Port des MQTT Servers angegeben. IN diesem Fall läuft ein Mosquitto Server auf einem Linux-System unter der Adresse ``x.x.x.1`` und der Deye ist über WLAN-Stick unter der Adressse ``x.x.x.2`` ins Netzwerk eingebunden.

.. code:: bash

	$ cat config.env
	DEYE_LOGGER_IP_ADDRESS=x.x.x.2
	# DEYE_LOGGER_PORT=8899
	DEYE_LOGGER_SERIAL_NUMBER=XXXXXXX
	# DEYE_LOGGER_PROTOCOL=tcp
	# DEYE_LOGGER_MAX_REG_RANGE_LENGTH=256

	MQTT_HOST=x.x.x.1
	# MQTT_PORT=1883
	# MQTT_USERNAME=user
	# MQTT_PASSWORD=password
	# MQTT_TOPIC_PREFIX=deye
	# MQTT_TLS_ENABLED=true
	# MQTT_TLS_INSECURE=true
	# MQTT_TLS_CA_CERT_PATH=certs/ca.crt
	# MQTT_TLS_CLIENT_CERT_PATH=certs/client.crt
	# MQTT_TLS_CLIENT_KEY_PATH=certs/client.key

	# LOG_LEVEL=INFO
	# LOG_STREAM=STDOUT
	# PLUGINS_DIR=plugins
	# PLUGINS_ENABLED=deye_plugin_sample,deye_plugin_custom
	# DEYE_DATA_READ_INTERVAL=60
	# DEYE_PUBLISH_ON_CHANGE=false
	# DEYE_PUBLISH_ON_CHANGE_MAX_INTERVAL=360
	# DEYE_METRIC_GROUPS=deye_sg04lp3, deye_sg04lp3_battery, deye_sg04lp3_ups, deye_sg04lp3_timeofuse, deye_sg04lp3_generator, settings
	DEYE_METRIC_GROUPS=deye_sg04lp3,deye_sg04lp3_battery,deye_sg04lp3_ups,deye_sg04lp3_timeofuse,deye_sg04lp3_generator,settings

	# DEYE_FEATURE_MQTT_PUBLISHER=true
	# DEYE_FEATURE_TIME_OF_USE=false
	# DEYE_FEATURE_ACTIVE_POWER_REGULATION=false
	# DEYE_FEATURE_SET_TIME=false

	## Sample multiinverter configuration with two loggers
	#
	# DEYE_LOGGER_COUNT=2

	# DEYE_LOGGER_1_IP_ADDRESS=192.168.0.1
	# DEYE_LOGGER_1_SERIAL_NUMBER=1234567890
	# DEYE_LOGGER_1_PROTOCOL=at

	# DEYE_LOGGER_2_IP_ADDRESS=192.168.0.2
	# DEYE_LOGGER_2_SERIAL_NUMBER=1234567891
	# DEYE_LOGGER_2_PROTOCOL=at




Installation unter Verwendung von Docker
========================================

Auf dem zentralen Linux Server ``lx01`` läuft ein Mosquitto MQTT Server (ehemals Broker genannt) und eine Docker Instanz des :program:`ghcr.io/kbialek/deye-inverter-mqtt` Images.

Container Starten::

	docker run -d --name deye-mqtt \
		--env-file $HOME/prj/deye-inverter-mqtt/config.env \
		--restart unless-stopped \
		ghcr.io/kbialek/deye-inverter-mqtt

	``-d`` will detach the container, so it will run in the background

	``--restart=unless-stopped`` will make docker to restart the container on host reboot

Status des Docker Containers::

	$ docker ps
	CONTAINER ID   IMAGE                                COMMAND                  CREATED         STATUS                          PORTS                                                                     NAMES
	22087776b50c   ghcr.io/kbialek/deye-inverter-mqtt   "python ./deye_docke…"   3 weeks ago     Up 15 hours                                                                                               deye-mqtt

Stoppen und entfernen des Containers::

	docker stop deye-mqtt
	docker rm -v deye-mqtt

Logfiles inspizieren::

	docker logs deye-mqtt

Betrieb
=======

Mit :command:`mosquitto_sub` kann der MQTT Datenverkehr beobachtet werden::

	$ mosquitto_sub -h x.x.x.1 -t "deye/#" -F '@Y-@m-@d @H:@M:@S : %t : %p'
	2024-08-11 10:31:12 : deye/status : online
	2024-08-11 10:31:40 : deye/logger_status : online
	2024-08-11 10:31:40 : deye/dc/pv1/power : 4480.0
	2024-08-11 10:31:40 : deye/dc/pv2/power : 2069.0
	2024-08-11 10:31:40 : deye/dc/pv1/voltage : 599.5
	2024-08-11 10:31:40 : deye/dc/pv2/voltage : 575.0
	2024-08-11 10:31:40 : deye/dc/pv1/current : 7.5
	2024-08-11 10:31:40 : deye/dc/pv2/current : 3.6
	2024-08-11 10:31:40 : deye/day_energy : 14.3
	2024-08-11 10:31:40 : deye/total_energy : 2030.7
	2024-08-11 10:31:40 : deye/battery/daily_charge : 8.4
	2024-08-11 10:31:40 : deye/battery/daily_discharge : 7.3
	2024-08-11 10:31:40 : deye/battery/total_charge : 356.8
	2024-08-11 10:31:40 : deye/battery/total_discharge : 331.5
	2024-08-11 10:31:40 : deye/battery/power : -6316.0
	2024-08-11 10:31:40 : deye/battery/voltage : 55.2
	2024-08-11 10:31:40 : deye/battery/soc : 93.0
	2024-08-11 10:31:40 : deye/battery/current : -114.5
	2024-08-11 10:31:40 : deye/battery/temperature : 25.0
	2024-08-11 10:31:40 : deye/ac/total_power : -4116.0
	2024-08-11 10:31:40 : deye/ac/l1/voltage : 236.0
	2024-08-11 10:31:40 : deye/ac/l2/voltage : 237.2
	2024-08-11 10:31:40 : deye/ac/l3/voltage : 235.9
	2024-08-11 10:31:40 : deye/ac/l1/ct/internal : 27.0
	2024-08-11 10:31:40 : deye/ac/l2/ct/internal : 30.0
	2024-08-11 10:31:40 : deye/ac/l3/ct/internal : -8.0
	2024-08-11 10:31:40 : deye/ac/l1/ct/external : -1940.0
	2024-08-11 10:31:40 : deye/ac/l2/ct/external : -1131.0
	2024-08-11 10:31:40 : deye/ac/l3/ct/external : -1045.0
	2024-08-11 10:31:40 : deye/ac/daily_energy_bought : 0.6
	2024-08-11 10:31:40 : deye/ac/total_energy_bought : 51.4
	2024-08-11 10:31:40 : deye/ac/daily_energy_sold : 0.8
	2024-08-11 10:31:40 : deye/ac/total_energy_sold : 1652.5
	2024-08-11 10:31:40 : deye/ac/ups/total_power : 0.0
	2024-08-11 10:31:40 : deye/ac/ups/l1/power : 0.0
	2024-08-11 10:31:40 : deye/ac/ups/l2/power : 0.0
	2024-08-11 10:31:40 : deye/ac/ups/l3/power : 0.0
	2024-08-11 10:31:40 : deye/ac/ups/l1/voltage : 235.7
	2024-08-11 10:31:40 : deye/ac/ups/l2/voltage : 236.1
	2024-08-11 10:31:40 : deye/ac/ups/l3/voltage : 236.6
	2024-08-11 10:31:40 : deye/ac/ups/daily_energy : 13.0
	2024-08-11 10:31:40 : deye/ac/ups/total_energy : 771.9
	2024-08-11 10:31:40 : deye/ac/l1/current : -0.3
	2024-08-11 10:31:40 : deye/ac/l2/current : -0.3
	2024-08-11 10:31:40 : deye/ac/l3/current : 0.0
	2024-08-11 10:31:40 : deye/ac/l1/power : -31.0
	2024-08-11 10:31:40 : deye/ac/l2/power : -43.0
	2024-08-11 10:31:40 : deye/ac/l3/power : 31.0
	2024-08-11 10:31:40 : deye/radiator_temp : 25.0
	2024-08-11 10:31:40 : deye/ac/temperature : 52.8
	2024-08-11 10:31:40 : deye/timeofuse/selling : 255.0
	2024-08-11 10:31:40 : deye/timeofuse/time/1 : 100.0
	2024-08-11 10:31:40 : deye/timeofuse/time/2 : 500.0
	2024-08-11 10:31:40 : deye/timeofuse/time/3 : 900.0
	2024-08-11 10:31:40 : deye/timeofuse/time/4 : 1300.0
	2024-08-11 10:31:40 : deye/timeofuse/time/5 : 1700.0
	2024-08-11 10:31:40 : deye/timeofuse/time/6 : 2100.0
	2024-08-11 10:31:40 : deye/timeofuse/power/1 : 12000.0
	2024-08-11 10:31:40 : deye/timeofuse/power/2 : 12000.0
	2024-08-11 10:31:40 : deye/timeofuse/power/3 : 12000.0
	2024-08-11 10:31:40 : deye/timeofuse/power/4 : 12000.0
	2024-08-11 10:31:40 : deye/timeofuse/power/5 : 12000.0
	2024-08-11 10:31:40 : deye/timeofuse/power/6 : 12000.0
	2024-08-11 10:31:40 : deye/timeofuse/voltage/1 : 49.0
	2024-08-11 10:31:40 : deye/timeofuse/voltage/2 : 49.0
	2024-08-11 10:31:40 : deye/timeofuse/voltage/3 : 49.0
	2024-08-11 10:31:40 : deye/timeofuse/voltage/4 : 49.0
	2024-08-11 10:31:40 : deye/timeofuse/voltage/5 : 49.0
	2024-08-11 10:31:40 : deye/timeofuse/voltage/6 : 49.0
	2024-08-11 10:31:40 : deye/timeofuse/soc/1 : 70.0
	2024-08-11 10:31:40 : deye/timeofuse/soc/2 : 30.0
	2024-08-11 10:31:40 : deye/timeofuse/soc/3 : 80.0
	2024-08-11 10:31:40 : deye/timeofuse/soc/4 : 80.0
	2024-08-11 10:31:40 : deye/timeofuse/soc/5 : 50.0
	2024-08-11 10:31:40 : deye/timeofuse/soc/6 : 50.0
	2024-08-11 10:31:40 : deye/timeofuse/enabled/1 : 0.0
	2024-08-11 10:31:40 : deye/timeofuse/enabled/2 : 0.0
	2024-08-11 10:31:40 : deye/timeofuse/enabled/3 : 0.0
	2024-08-11 10:31:40 : deye/timeofuse/enabled/4 : 0.0
	2024-08-11 10:31:40 : deye/timeofuse/enabled/5 : 0.0
	2024-08-11 10:31:40 : deye/timeofuse/enabled/6 : 0.0
	2024-08-11 10:31:40 : deye/ac/generator/a/voltage : 0.7
	2024-08-11 10:31:40 : deye/ac/generator/b/voltage : 0.3
	2024-08-11 10:31:40 : deye/ac/generator/c/voltage : 0.4
	2024-08-11 10:31:40 : deye/ac/generator/a/power : 0.0
	2024-08-11 10:31:40 : deye/ac/generator/b/power : 0.0
	2024-08-11 10:31:40 : deye/ac/generator/c/power : 0.0
	2024-08-11 10:31:40 : deye/ac/generator/total_power : 0.0
	2024-08-11 10:31:40 : deye/ac/generator/daily_energy : 0.0
	2024-08-11 10:31:40 : deye/settings/active_power_regulation : 0.0


Einbinden in FHEM
=================


.. seealso::

	- `<https://wiki.fhem.de/wiki/MQTT2-Module_-_Praxisbeispiele>`_
	- `<https://wiki.fhem.de/wiki/MQTT2_DEVICE_-_Schritt_f%C3%BCr_Schritt>`_
	- `<https://wiki.fhem.de/wiki/MQTT_GENERIC_BRIDGE>`_

Bei aktiviertem `autocreate` legt FHEM bei Eintreffen von MQTT-Nachrichten automatisch für jedes Device eine Instanz des Modules `MQTT2_DEVICE` an.

Wenn ein externer MQTT-Server zum Einsatz kommt, ist sehr zu empfehlen, für die Beschäftigung mit einem neuen, unbekannten Device zunächst einen MQTT2_SERVER einzurichten. Ist der Port 1883 bereits belegt, nimmt man einfach einen anderen Port, z.B. 1884::

	define m2server MQTT2_SERVER 1884 global

	list m2server

	Internals:
	CFGFN
	CONNECTS   2
	Clients    :MQTT2_DEVICE:MQTT_GENERIC_BRIDGE:
	ClientsKeepOrder 1
	DEF        1884 global
	FD         74
	FUUID      66b8870d-f33f-d1b0-0f65-f56c8dec9410ebb8
	NAME       m2server
	NR         408
	PORT       1884
	STATE      Initialized
	TYPE       MQTT2_SERVER
	eventCount 3
	Helper:
		DBLOG:
		nrclients:
			logdb:
			TIME       1723370775.21739
			VALUE      1
	MatchList:
		1:MQTT2_DEVICE ^.
		2:MQTT_GENERIC_BRIDGE ^.
	READINGS:
		2024-08-11 12:06:15   nrclients       1
		2024-08-11 11:40:29   state           Initialized
	clients:
		m2server_172.18.0.3_53645 1
	hmccu:
	retain:
	Attributes:
	autocreate simple
	mqttAlias  MQTT autocreate Testserver
	room       Technik


Dies verhindert auch, dass mit ``autocreate`` beim Standard-MQTT-Server nicht undefiniert MQTT2 Devices anlegt. Beim Testserver wird `attr mqtt autocreate simple` gesetzt.


Jetzt muss temporär die Dockerinstanz von :program:`deye-mqtt` temporär auf auf Port 1884 umgestellt werden, dazu wird die config.env geändert und die Instanz neu generiert::

	docker stop deye-mqtt
	docker rm -v deye-mqtt
	docker run -d --name deye-mqtt --env-file $HOME/prj/deye-inverter-mqtt/config.env --restart unless-stopped ghcr.io/kbialek/deye-inverter-mqtt

Der DEYE Inverter wird automatisch angelegt, allerdings gibt es einige FHEM-Werte, die mehrfach belegt sind und somit überschrieben werden::

	list deye_inverter_nnnnnnnn

	Internals:
	CFGFN
	CID        deye_inverter_nnnnnnnn
	DEF        deye_inverter_nnnnnnnn
	FUUID      66b88d18-f33f-d1b0-18fe-12286307fbce0ba7
	IODev      m2server
	LASTInputDev m2server
	MSGCNT     979
	NAME       MQTT2_deye_inverter_nnnnnnnn
	NR         409
	STATE      ???
	TYPE       MQTT2_DEVICE
	eventCount 1069
	m2server_CONN m2server_172.18.0.3_53645
	m2server_MSGCNT 979
	m2server_TIME 2024-08-11 12:17:40
	Helper:
		DBLOG:
		active_power_regulation:
			logdb:
			TIME       1723371460.2513
			VALUE      0.0
		current:
			logdb:
			TIME       1723371460.19088
			VALUE      -1.1
		daily_charge:
			logdb:
			TIME       1723371460.13956
			VALUE      10.9
		daily_discharge:
			logdb:
			TIME       1723371460.14098
			VALUE      7.3
		daily_energy:
			logdb:
			TIME       1723371460.24999
			VALUE      0.0
		daily_energy_bought:
			logdb:
			TIME       1723371460.17016
			VALUE      0.6
		daily_energy_sold:
			logdb:
			TIME       1723371460.17276
			VALUE      13.1
		day_energy:
			logdb:
			TIME       1723371460.13614
			VALUE      24.4
		enabled_1:
			logdb:
			TIME       1723371460.23268
			VALUE      0.0
		enabled_2:
			logdb:
			TIME       1723371460.23397
			VALUE      0.0
		enabled_3:
			logdb:
			TIME       1723371460.23521
			VALUE      0.0
		enabled_4:
			logdb:
			TIME       1723371460.23643
			VALUE      0.0
		enabled_5:
			logdb:
			TIME       1723371460.23766
			VALUE      0.0
		enabled_6:
			logdb:
			TIME       1723371460.23884
			VALUE      0.0
		external:
			logdb:
			TIME       1723371460.16886
			VALUE      -3015.0
		internal:
			logdb:
			TIME       1723371460.16492
			VALUE      181.0
		logger_status:
			logdb:
			TIME       1723371460.12659
			VALUE      online
		power:
			logdb:
			TIME       1723371460.24722
			VALUE      0.0
		power_1:
			logdb:
			TIME       1723371460.20813
			VALUE      12000.0
		power_2:
			logdb:
			TIME       1723371460.20978
			VALUE      12000.0
		power_3:
			logdb:
			TIME       1723371460.21131
			VALUE      12000.0
		power_4:
			logdb:
			TIME       1723371460.2126
			VALUE      12000.0
		power_5:
			logdb:
			TIME       1723371460.21385
			VALUE      12000.0
		power_6:
			logdb:
			TIME       1723371460.21513
			VALUE      12000.0
		radiator_temp:
			logdb:
			TIME       1723371460.19675
			VALUE      25.0
		selling:
			logdb:
			TIME       1723371460.19921
			VALUE      255.0
		soc:
			logdb:
			TIME       1723371460.14698
			VALUE      100.0
		soc_1:
			logdb:
			TIME       1723371460.2244
			VALUE      70.0
		soc_2:
			logdb:
			TIME       1723371460.22565
			VALUE      30.0
		soc_3:
			logdb:
			TIME       1723371460.22689
			VALUE      80.0
		soc_4:
			logdb:
			TIME       1723371460.22858
			VALUE      80.0
		soc_5:
			logdb:
			TIME       1723371460.23009
			VALUE      50.0
		soc_6:
			logdb:
			TIME       1723371460.2314
			VALUE      50.0
		status:
			logdb:
			TIME       1723370776.24225
			VALUE      online
		temperature:
			logdb:
			TIME       1723371460.19804
			VALUE      51.2
		time_1:
			logdb:
			TIME       1723371460.2004
			VALUE      100.0
		time_2:
			logdb:
			TIME       1723371460.20177
			VALUE      500.0
		time_3:
			logdb:
			TIME       1723371460.20306
			VALUE      900.0
		time_4:
			logdb:
			TIME       1723371460.20436
			VALUE      1300.0
		time_5:
			logdb:
			TIME       1723371460.20558
			VALUE      1700.0
		time_6:
			logdb:
			TIME       1723371460.2069
			VALUE      2100.0
		total_charge:
			logdb:
			TIME       1723371460.1422
			VALUE      359.4
		total_discharge:
			logdb:
			TIME       1723371460.1433
			VALUE      331.5
		total_energy:
			logdb:
			TIME       1723371460.18674
			VALUE      771.9
		total_energy_bought:
			logdb:
			TIME       1723371460.17143
			VALUE      51.4
		total_energy_sold:
			logdb:
			TIME       1723371460.17474
			VALUE      1664.8
		total_power:
			logdb:
			TIME       1723371460.24863
			VALUE      0.0
		voltage:
			logdb:
			TIME       1723371460.24256
			VALUE      0.5
		voltage_1:
			logdb:
			TIME       1723371460.21632
			VALUE      49.0
		voltage_2:
			logdb:
			TIME       1723371460.21758
			VALUE      49.0
		voltage_3:
			logdb:
			TIME       1723371460.21905
			VALUE      49.0
		voltage_4:
			logdb:
			TIME       1723371460.22035
			VALUE      49.0
		voltage_5:
			logdb:
			TIME       1723371460.22182
			VALUE      49.0
		voltage_6:
			logdb:
			TIME       1723371460.22314
			VALUE      49.0
	READINGS:
		2024-08-11 12:06:16   IODev           m2server
		2024-08-11 12:17:40   active_power_regulation 0.0
		2024-08-11 12:17:40   current         -1.1
		2024-08-11 12:17:40   daily_charge    10.9
		2024-08-11 12:17:40   daily_discharge 7.3
		2024-08-11 12:17:40   daily_energy    0.0
		2024-08-11 12:17:40   daily_energy_bought 0.6
		2024-08-11 12:17:40   daily_energy_sold 13.1
		2024-08-11 12:17:40   day_energy      24.4
		2024-08-11 12:17:40   enabled_1       0.0
		2024-08-11 12:17:40   enabled_2       0.0
		2024-08-11 12:17:40   enabled_3       0.0
		2024-08-11 12:17:40   enabled_4       0.0
		2024-08-11 12:17:40   enabled_5       0.0
		2024-08-11 12:17:40   enabled_6       0.0
		2024-08-11 12:17:40   external        -3015.0
		2024-08-11 12:17:40   internal        181.0
		2024-08-11 12:17:40   logger_status   online
		2024-08-11 12:17:40   power           0.0
		2024-08-11 12:17:40   power_1         12000.0
		2024-08-11 12:17:40   power_2         12000.0
		2024-08-11 12:17:40   power_3         12000.0
		2024-08-11 12:17:40   power_4         12000.0
		2024-08-11 12:17:40   power_5         12000.0
		2024-08-11 12:17:40   power_6         12000.0
		2024-08-11 12:17:40   radiator_temp   25.0
		2024-08-11 12:17:40   selling         255.0
		2024-08-11 12:17:40   soc             100.0
		2024-08-11 12:17:40   soc_1           70.0
		2024-08-11 12:17:40   soc_2           30.0
		2024-08-11 12:17:40   soc_3           80.0
		2024-08-11 12:17:40   soc_4           80.0
		2024-08-11 12:17:40   soc_5           50.0
		2024-08-11 12:17:40   soc_6           50.0
		2024-08-11 12:06:16   status          online
		2024-08-11 12:17:40   temperature     51.2
		2024-08-11 12:17:40   time_1          100.0
		2024-08-11 12:17:40   time_2          500.0
		2024-08-11 12:17:40   time_3          900.0
		2024-08-11 12:17:40   time_4          1300.0
		2024-08-11 12:17:40   time_5          1700.0
		2024-08-11 12:17:40   time_6          2100.0
		2024-08-11 12:17:40   total_charge    359.4
		2024-08-11 12:17:40   total_discharge 331.5
		2024-08-11 12:17:40   total_energy    771.9
		2024-08-11 12:17:40   total_energy_bought 51.4
		2024-08-11 12:17:40   total_energy_sold 1664.8
		2024-08-11 12:17:40   total_power     0.0
		2024-08-11 12:17:40   voltage         0.5
		2024-08-11 12:17:40   voltage_1       49.0
		2024-08-11 12:17:40   voltage_2       49.0
		2024-08-11 12:17:40   voltage_3       49.0
		2024-08-11 12:17:40   voltage_4       49.0
		2024-08-11 12:17:40   voltage_5       49.0
		2024-08-11 12:17:40   voltage_6       49.0
	hmccu:
	Attributes:
	readingList deye_inverter_nnnnnnnn:deye/status:.* status
	deye_inverter_nnnnnnnn:deye/logger_status:.* logger_status
	deye_inverter_nnnnnnnn:deye/dc/pv1/power:.* power
	deye_inverter_nnnnnnnn:deye/dc/pv2/power:.* power
	deye_inverter_nnnnnnnn:deye/dc/pv1/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/dc/pv2/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/dc/pv1/current:.* current
	deye_inverter_nnnnnnnn:deye/dc/pv2/current:.* current
	deye_inverter_nnnnnnnn:deye/day_energy:.* day_energy
	deye_inverter_nnnnnnnn:deye/total_energy:.* total_energy
	deye_inverter_nnnnnnnn:deye/battery/daily_charge:.* daily_charge
	deye_inverter_nnnnnnnn:deye/battery/daily_discharge:.* daily_discharge
	deye_inverter_nnnnnnnn:deye/battery/total_charge:.* total_charge
	deye_inverter_nnnnnnnn:deye/battery/total_discharge:.* total_discharge
	deye_inverter_nnnnnnnn:deye/battery/power:.* power
	deye_inverter_nnnnnnnn:deye/battery/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/battery/soc:.* soc
	deye_inverter_nnnnnnnn:deye/battery/current:.* current
	deye_inverter_nnnnnnnn:deye/battery/temperature:.* temperature
	deye_inverter_nnnnnnnn:deye/ac/total_power:.* total_power
	deye_inverter_nnnnnnnn:deye/ac/l1/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/ac/l2/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/ac/l3/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/ac/l1/ct/internal:.* internal
	deye_inverter_nnnnnnnn:deye/ac/l2/ct/internal:.* internal
	deye_inverter_nnnnnnnn:deye/ac/l3/ct/internal:.* internal
	deye_inverter_nnnnnnnn:deye/ac/l1/ct/external:.* external
	deye_inverter_nnnnnnnn:deye/ac/l2/ct/external:.* external
	deye_inverter_nnnnnnnn:deye/ac/l3/ct/external:.* external
	deye_inverter_nnnnnnnn:deye/ac/daily_energy_bought:.* daily_energy_bought
	deye_inverter_nnnnnnnn:deye/ac/total_energy_bought:.* total_energy_bought
	deye_inverter_nnnnnnnn:deye/ac/daily_energy_sold:.* daily_energy_sold
	deye_inverter_nnnnnnnn:deye/ac/total_energy_sold:.* total_energy_sold
	deye_inverter_nnnnnnnn:deye/ac/ups/total_power:.* total_power
	deye_inverter_nnnnnnnn:deye/ac/ups/l1/power:.* power
	deye_inverter_nnnnnnnn:deye/ac/ups/l2/power:.* power
	deye_inverter_nnnnnnnn:deye/ac/ups/l3/power:.* power
	deye_inverter_nnnnnnnn:deye/ac/ups/l1/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/ac/ups/l2/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/ac/ups/l3/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/ac/ups/daily_energy:.* daily_energy
	deye_inverter_nnnnnnnn:deye/ac/ups/total_energy:.* total_energy
	deye_inverter_nnnnnnnn:deye/ac/l1/current:.* current
	deye_inverter_nnnnnnnn:deye/ac/l2/current:.* current
	deye_inverter_nnnnnnnn:deye/ac/l3/current:.* current
	deye_inverter_nnnnnnnn:deye/ac/l1/power:.* power
	deye_inverter_nnnnnnnn:deye/ac/l2/power:.* power
	deye_inverter_nnnnnnnn:deye/ac/l3/power:.* power
	deye_inverter_nnnnnnnn:deye/radiator_temp:.* radiator_temp
	deye_inverter_nnnnnnnn:deye/ac/temperature:.* temperature
	deye_inverter_nnnnnnnn:deye/timeofuse/selling:.* selling
	deye_inverter_nnnnnnnn:deye/timeofuse/time/1:.* time_1
	deye_inverter_nnnnnnnn:deye/timeofuse/time/2:.* time_2
	deye_inverter_nnnnnnnn:deye/timeofuse/time/3:.* time_3
	deye_inverter_nnnnnnnn:deye/timeofuse/time/4:.* time_4
	deye_inverter_nnnnnnnn:deye/timeofuse/time/5:.* time_5
	deye_inverter_nnnnnnnn:deye/timeofuse/time/6:.* time_6
	deye_inverter_nnnnnnnn:deye/timeofuse/power/1:.* power_1
	deye_inverter_nnnnnnnn:deye/timeofuse/power/2:.* power_2
	deye_inverter_nnnnnnnn:deye/timeofuse/power/3:.* power_3
	deye_inverter_nnnnnnnn:deye/timeofuse/power/4:.* power_4
	deye_inverter_nnnnnnnn:deye/timeofuse/power/5:.* power_5
	deye_inverter_nnnnnnnn:deye/timeofuse/power/6:.* power_6
	deye_inverter_nnnnnnnn:deye/timeofuse/voltage/1:.* voltage_1
	deye_inverter_nnnnnnnn:deye/timeofuse/voltage/2:.* voltage_2
	deye_inverter_nnnnnnnn:deye/timeofuse/voltage/3:.* voltage_3
	deye_inverter_nnnnnnnn:deye/timeofuse/voltage/4:.* voltage_4
	deye_inverter_nnnnnnnn:deye/timeofuse/voltage/5:.* voltage_5
	deye_inverter_nnnnnnnn:deye/timeofuse/voltage/6:.* voltage_6
	deye_inverter_nnnnnnnn:deye/timeofuse/soc/1:.* soc_1
	deye_inverter_nnnnnnnn:deye/timeofuse/soc/2:.* soc_2
	deye_inverter_nnnnnnnn:deye/timeofuse/soc/3:.* soc_3
	deye_inverter_nnnnnnnn:deye/timeofuse/soc/4:.* soc_4
	deye_inverter_nnnnnnnn:deye/timeofuse/soc/5:.* soc_5
	deye_inverter_nnnnnnnn:deye/timeofuse/soc/6:.* soc_6
	deye_inverter_nnnnnnnn:deye/timeofuse/enabled/1:.* enabled_1
	deye_inverter_nnnnnnnn:deye/timeofuse/enabled/2:.* enabled_2
	deye_inverter_nnnnnnnn:deye/timeofuse/enabled/3:.* enabled_3
	deye_inverter_nnnnnnnn:deye/timeofuse/enabled/4:.* enabled_4
	deye_inverter_nnnnnnnn:deye/timeofuse/enabled/5:.* enabled_5
	deye_inverter_nnnnnnnn:deye/timeofuse/enabled/6:.* enabled_6
	deye_inverter_nnnnnnnn:deye/ac/generator/a/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/ac/generator/b/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/ac/generator/c/voltage:.* voltage
	deye_inverter_nnnnnnnn:deye/ac/generator/a/power:.* power
	deye_inverter_nnnnnnnn:deye/ac/generator/b/power:.* power
	deye_inverter_nnnnnnnn:deye/ac/generator/c/power:.* power
	deye_inverter_nnnnnnnn:deye/ac/generator/total_power:.* total_power
	deye_inverter_nnnnnnnn:deye/ac/generator/daily_energy:.* daily_energy
	deye_inverter_nnnnnnnn:deye/settings/active_power_regulation:.* active_power_regulation
	room       MQTT2_DEVICE



Die Zuweisungen werden jetzt in FHEM auf eindeutige Benennungen angepasst und das Device umgestellt::

	attr MQTT2_deye_inverter_nnnnnnnn IODev mqtt
	attr mqttGeneric subscriptions deye/#:deye_inverter_

	deye_inverter_2798476009:deye/status:.* status
	deye_inverter_2798476009:deye/logger_status:.* logger_status
	deye_inverter_2798476009:deye/dc/pv1/power:.* pv1_power
	deye_inverter_2798476009:deye/dc/pv2/power:.* pv2_power
	deye_inverter_2798476009:deye/dc/pv1/voltage:.* pv1_voltage
	deye_inverter_2798476009:deye/dc/pv2/voltage:.* pv2_voltage
	deye_inverter_2798476009:deye/dc/pv1/current:.* pv1_current
	deye_inverter_2798476009:deye/dc/pv2/current:.* pv2_current
	deye_inverter_2798476009:deye/day_energy:.* day_energy
	deye_inverter_2798476009:deye/total_energy:.* total_energy
	deye_inverter_2798476009:deye/battery/daily_charge:.* battery_daily_charge
	deye_inverter_2798476009:deye/battery/daily_discharge:.* battery_daily_discharge
	deye_inverter_2798476009:deye/battery/total_charge:.* battery_total_charge
	deye_inverter_2798476009:deye/battery/total_discharge:.* battery_total_discharge
	deye_inverter_2798476009:deye/battery/power:.* battery_power
	deye_inverter_2798476009:deye/battery/voltage:.* battery_voltage
	deye_inverter_2798476009:deye/battery/soc:.* battery_soc
	deye_inverter_2798476009:deye/battery/current:.* battery_current
	deye_inverter_2798476009:deye/battery/temperature:.* battery_temperature
	deye_inverter_2798476009:deye/ac/total_power:.* ac_total_power
	deye_inverter_2798476009:deye/ac/l1/voltage:.* acl1_voltage
	deye_inverter_2798476009:deye/ac/l2/voltage:.* acl2_voltage
	deye_inverter_2798476009:deye/ac/l3/voltage:.* acl3_voltage
	deye_inverter_2798476009:deye/ac/l1/ct/internal:.* acl1_internal
	deye_inverter_2798476009:deye/ac/l2/ct/internal:.* acl2_internal
	deye_inverter_2798476009:deye/ac/l3/ct/internal:.* acl3_internal
	deye_inverter_2798476009:deye/ac/l1/ct/external:.* acl1_external
	deye_inverter_2798476009:deye/ac/l2/ct/external:.* acl2_external
	deye_inverter_2798476009:deye/ac/l3/ct/external:.* acl3_external
	deye_inverter_2798476009:deye/ac/daily_energy_bought:.* daily_energy_bought
	deye_inverter_2798476009:deye/ac/total_energy_bought:.* total_energy_bought
	deye_inverter_2798476009:deye/ac/daily_energy_sold:.* daily_energy_sold
	deye_inverter_2798476009:deye/ac/total_energy_sold:.* total_energy_sold
	deye_inverter_2798476009:deye/ac/ups/total_power:.* ups_total_power
	deye_inverter_2798476009:deye/ac/ups/l1/power:.* upsl1_power
	deye_inverter_2798476009:deye/ac/ups/l2/power:.* upsl2_power
	deye_inverter_2798476009:deye/ac/ups/l3/power:.* up2l3_power
	deye_inverter_2798476009:deye/ac/ups/l1/voltage:.* upsl1_voltage
	deye_inverter_2798476009:deye/ac/ups/l2/voltage:.* upsl2_voltage
	deye_inverter_2798476009:deye/ac/ups/l3/voltage:.* upsl3_voltage
	deye_inverter_2798476009:deye/ac/ups/daily_energy:.* ups_daily_energy
	deye_inverter_2798476009:deye/ac/ups/total_energy:.* ups_total_energy
	deye_inverter_2798476009:deye/ac/l1/current:.* acl1_current
	deye_inverter_2798476009:deye/ac/l2/current:.* acl2_current
	deye_inverter_2798476009:deye/ac/l3/current:.* acl3_current
	deye_inverter_2798476009:deye/ac/l1/power:.* acl1_power
	deye_inverter_2798476009:deye/ac/l2/power:.* acl2_power
	deye_inverter_2798476009:deye/ac/l3/power:.* acl3_power
	deye_inverter_2798476009:deye/radiator_temp:.* radiator_temp
	deye_inverter_2798476009:deye/ac/temperature:.* ac_temperature
	deye_inverter_2798476009:deye/timeofuse/selling:.* timeofuse_selling
	deye_inverter_2798476009:deye/timeofuse/time/1:.* timeofuse_time_1
	deye_inverter_2798476009:deye/timeofuse/time/2:.* timeofuse_time_2
	deye_inverter_2798476009:deye/timeofuse/time/3:.* timeofuse_time_3
	deye_inverter_2798476009:deye/timeofuse/time/4:.* timeofuse_time_4
	deye_inverter_2798476009:deye/timeofuse/time/5:.* timeofuse_time_5
	deye_inverter_2798476009:deye/timeofuse/time/6:.* timeofuse_time_6
	deye_inverter_2798476009:deye/timeofuse/power/1:.* timeofuse_power_1
	deye_inverter_2798476009:deye/timeofuse/power/2:.* timeofuse_power_2
	deye_inverter_2798476009:deye/timeofuse/power/3:.* timeofuse_power_3
	deye_inverter_2798476009:deye/timeofuse/power/4:.* timeofuse_power_4
	deye_inverter_2798476009:deye/timeofuse/power/5:.* timeofuse_power_5
	deye_inverter_2798476009:deye/timeofuse/power/6:.* timeofuse_power_6
	deye_inverter_2798476009:deye/timeofuse/voltage/1:.* timeofuse_voltage_1
	deye_inverter_2798476009:deye/timeofuse/voltage/2:.* timeofuse_voltage_2
	deye_inverter_2798476009:deye/timeofuse/voltage/3:.* timeofuse_voltage_3
	deye_inverter_2798476009:deye/timeofuse/voltage/4:.* timeofuse_voltage_4
	deye_inverter_2798476009:deye/timeofuse/voltage/5:.* timeofuse_voltage_5
	deye_inverter_2798476009:deye/timeofuse/voltage/6:.* timeofuse_voltage_6
	deye_inverter_2798476009:deye/timeofuse/soc/1:.* timeofuse_soc_1
	deye_inverter_2798476009:deye/timeofuse/soc/2:.* timeofuse_soc_2
	deye_inverter_2798476009:deye/timeofuse/soc/3:.* timeofuse_soc_3
	deye_inverter_2798476009:deye/timeofuse/soc/4:.* timeofuse_soc_4
	deye_inverter_2798476009:deye/timeofuse/soc/5:.* timeofuse_soc_5
	deye_inverter_2798476009:deye/timeofuse/soc/6:.* timeofuse_soc_6
	deye_inverter_2798476009:deye/timeofuse/enabled/1:.* timeofuse_enabled_1
	deye_inverter_2798476009:deye/timeofuse/enabled/2:.* timeofuse_enabled_2
	deye_inverter_2798476009:deye/timeofuse/enabled/3:.* timeofuse_enabled_3
	deye_inverter_2798476009:deye/timeofuse/enabled/4:.* timeofuse_enabled_4
	deye_inverter_2798476009:deye/timeofuse/enabled/5:.* timeofuse_enabled_5
	deye_inverter_2798476009:deye/timeofuse/enabled/6:.* timeofuse_enabled_6
	deye_inverter_2798476009:deye/ac/generator/a/voltage:.* generator_a_voltage
	deye_inverter_2798476009:deye/ac/generator/b/voltage:.* generator_b_voltage
	deye_inverter_2798476009:deye/ac/generator/c/voltage:.* generator_c_voltage
	deye_inverter_2798476009:deye/ac/generator/a/power:.* generator_a_power
	deye_inverter_2798476009:deye/ac/generator/b/power:.* generator_b_power
	deye_inverter_2798476009:deye/ac/generator/c/power:.* generator_c_power
	deye_inverter_2798476009:deye/ac/generator/total_power:.* generator_total_power
	deye_inverter_2798476009:deye/ac/generator/daily_energy:.* generator_daily_energy
	deye_inverter_2798476009:deye/settings/active_power_regulation:.* active_power_regulation

