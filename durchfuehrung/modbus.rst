##################################
Geräte mit Modbus Interface
##################################

NIBE 1255 / 1256 Modbus Interface
=================================

.. seealso:: https://github.com/henningms/nibe-s1255-modbus


.. only:: html

	.. csv-table:: NIBE Modbus-Register, exportiert via USB Interface
		:header-rows: 1
		:file: ./csv/nibe-1256-modbus-en.csv
		:delim: ;
		:stub-columns: 1
		:end-line: 200





Modbus zu MQTT
==============

Damit die Werte aus der NIBE S1256 gut in die bestehende Hausautomatisierung integriert werden können, ist eine Umsetzung der Modbus-Werte auf MQTT ein vielversprechender Ansatz.

.. seealso::

	https://github.com/yozik04/nibe-mqtt

.. code:: bash

	$ cat config.yaml
	logging:
	level: INFO
	format: "%(asctime)s - %(levelname)-8s - %(threadName)-10s - %(name)s - %(message)s"
	mqtt:
	host: 172.30.2.6
	port: 1883
	protocol: 5
	nibe:
	model: S1256
	word_swap: true
	modbus:
		url: tcp://NIBE-06571123352007.web-me.local:502
		slave_id: 1
	poll:
		interval: 30
		coils:
		- current-outdoor-temperature-bt1-30002


.. code:: bash

	docker run -ti --pull=always --rm -p 9999:9999/udp -v "/home/rainerth/prj/nibe-mqtt/config.yaml:/config/nibe-mqtt/config.yaml:ro" yozik04/nibe-mqtt:latest

