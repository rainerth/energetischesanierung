################################
Persistierung und Visualisierung
################################


Eine Docker-Instanz von Telegraf wird verwendet, um Daten aus MQTT in die influxDB zu kopieren. Die Konfiguration von Telegraf ist sehr umfangreicht. Nach Änderungen empfiehlt es sich, die Konfiguration überprüfen::

	docker run --rm -v /home/rainerth/docker/telegraf/telegraf.conf:/etc/telegraf/telegraf.conf:ro telegraf --config /etc/telegraf/telegraf.conf --test

Danach wird die Telegraf-Instanz gestartet::

	docker run -d --name=telegraf -v /home/rainerth/docker/telegraf/telegraf.conf:/etc/telegraf/telegraf.conf:ro --network=bridge telegraf


Konfiguration
=============

:file:`~/docker/telegraf/telegraf.conf`, Stand Oktober 2026::

	[[outputs.influxdb_v2]]
		urls = ["http://172.30.2.6:8086"]
		token = "xxxx...=="
		organization = "Homeautomation"
		bucket = "rth-merowingerstr"

	[[inputs.mqtt_consumer]]
		servers = ["tcp://172.30.2.6:1883"]
		topics = [
		"nibe/coils/#",
		"openWB/bat/7/get/#",
		"openWB/pv/1/get/#",
		"openWB/pv/8/get/#",
		"deye/#",
		"sml/#",
		"hmip/+/+",
		]

.. list-table:: Woher die Daten kommen
	:header-rows: 1
	:stub-columns: 1

	*	-	Topic
		-	Quelle

	*	-	``nibe/coils/#``
		-	Wärmepumpe über ``nibe-mqtt``, ein Topic je Modbus-Register

	*	-	``deye/#``
		-	Hybridwechselrichter über ``deye-mqtt``

	*	-	``sml/#``
		-	die vier Energiezähler über die SML-Bridge

	*	-	``openWB/…``
		-	Wallbox und die von ihr geführten Zählerwerte

	*	-	``hmip/+/+``
		-	Raumtemperatur und Luftfeuchte der Funkthermostate

.. attention::

	Das Topic für die Wärmepumpe lautet ``nibe/coils/#`` und **nicht** ``nibe/#``. Die Bridge veröffentlicht unter ``nibe/`` auch Statusmeldungen, die keine Messwerte sind. Ein zu weit gefasstes Abonnement schreibt diese mit in die Datenbank.

	Ebenso ist der Zielbucket ``rth-merowingerstr``. Eine ältere Fassung dieser Dokumentation nannte hier ``fhem``; dieser Bucket gehört zu einer anderen Datenquelle.
