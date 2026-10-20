##################################
Geräte mit Modbus Interface
##################################

NIBE 1255 / 1256 Modbus Interface
=================================

.. seealso::

	* :download:`NIBE_IH_Modbus_mit_S-Serie_V2418 </_static/datenblaetter/NIBE_IH_Modbus_mit_S-Serie_V2418.pdf>`
	* https://github.com/henningms/nibe-s1255-modbus

.. attention::

	In diversen Foren ist zu lesen, man solle bei der NIBE nicht zu häufig schreiben, weil das den internen Speicher schädigen könne. **Diese Behauptung ist nicht aus einer Herstellerquelle belegt**, weder im Installateurhandbuch noch in der technischen Information zu Modbus findet sich eine Aussage dazu.

	Unabhängig davon ist Zurückhaltung beim Schreiben sinnvoll: Einstellwerte ändern sich im normalen Betrieb nicht, ein zyklisches Schreiben hat also ohnehin keinen Zweck. Lesen ist davon nicht betroffen.


mbpoll
======

Mit dem Command Line tool :command:`mbpoll` können Register der S1256 ausgelesen und geschrieben werden.

Beispiel: Auslesen des Registers 1 ``Current outdoor temperature (BT1)`` und 8,9 ``Hot Water Top``, ``Hot water charging (BT6)``::

	mbpoll 172.30.3.8 -0 -r 1 -t 3 -c 1
	-- Polling slave 1... Ctrl-C to stop)
	[1]: 	120

	mbpoll 172.30.3.8 -0 -r 8 -t 3 -c 2
	-- Polling slave 1... Ctrl-C to stop)
	[8]: 	463
	[9]: 	365

	mbpoll -h


Relevante NIBE MODBUS Register
==============================

Die Adressierung folgt der NIBE-Schreibweise: Holding-Register ``40001 + ID``, Input-Register ``30001 + ID``. Welche Register die Raumtemperatur beeinflussen und worauf dabei zu achten ist, steht in :doc:`raumtemperatur`.

AUX über Modbus
---------------

Eine AUX-Funktion lässt sich auch ohne physischen Kontakt über Modbus auslösen. Dazu wird die Funktions-ID in das Register **2740** geschrieben und der Zustand anschließend über Register **2741** gesetzt, mit 0 für aus und 1 für ein. Das Gerät braucht dafür mindestens Softwareversion 2.4.3.

.. attention::

	Es gibt nur einen solchen Kanal. Ist er bereits belegt, etwa um die Heizung bei geöffneter Tür zu blockieren (Funktions-ID 6), steht er für nichts anderes mehr zur Verfügung.



.. only:: html

	.. csv-table:: NIBE Modbus-Register, exportiert via USB Interface
		:header-rows: 1
		:file: ./csv/nibe-1256-modbus-en.csv
		:delim: ;
		:stub-columns: 1



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

