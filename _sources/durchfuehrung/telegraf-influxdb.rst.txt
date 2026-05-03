################################
Persistierung und Visualisierung
################################


Eine Docker-Instanz von Telegraf wird verwendet, um Daten aus MQTT in die influxDB zu kopieren. Die Konfiguration von Telegraf ist sehr umfangreicht. Nach Änderungen empfiehlt es sich, die Konfiguration überprüfen::

	docker run --rm -v /home/rainerth/docker/telegraf/telegraf.conf:/etc/telegraf/telegraf.conf:ro telegraf --config /etc/telegraf/telegraf.conf --test

Danach wird die Telegraf-Instanz gestartet::

	docker run -d --name=telegraf -v /home/rainerth/docker/telegraf/telegraf.conf:/etc/telegraf/telegraf.conf:ro --network=bridge telegraf


Konfiguration
=============

~/docker/telegraf/telegraf.conf::

	[[outputs.influxdb_v2]]
		urls = ["http://172.30.2.6:8086"]
		token = "xxxx...=="
		organization = "Homeautomation"
		bucket = "fhem"

	[[inputs.mqtt_consumer]]
		servers = ["tcp://172.30.2.6:1883"]
		topics = [
		"nibe/#",
		"openWB/bat/7/get/#",
		"openWB/pv/1/get/#",
		"openWB/pv/8/get/#",
		"deye/#",
		]
