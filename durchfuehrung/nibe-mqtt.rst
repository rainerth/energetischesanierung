##############################################
Einbindung der NIBE-S1256 Wärmempumpe via MQTT
##############################################

Die NIBE Wärmempumpe liefert per Modbus/TCP alle relevanten Werte. Mit zwei Github-Projekten können diese Werte in den MQTT Baum übernommen werden.


Das `Github Projekt yozik04/nibe <https://github.com/yozik04/nibe/tree/master>`_ beschreibt und ermöglicht den Zugriff auf die Modbusregister der NIBES1256.

Das `Github Projekt yozik04/nibe-mqtt <https://github.com/yozik04/nibe-mqtt>` liest die Register der NIBE-S1256 (und anderen) aus uns überträgt sie in den MQTT Baum.


Ermitteln der Modbus/TCP Register
=================================

.. attention:: Die Sprache muss aktuell auf Englisch umgestellt werden, damit die Menüpunkte für die Registerausgabe erscheinen.

Die Daten werden dann in das data-Verzeichnis des Projekts kopiert (:file:`~/prj/nibe/nibe/data`). Die CSV-Datei ist eine Quelldatei für den weiteren Prozess und darf nicht geändert werden.

.. code:: bash

	cd ~/prj/nibe/nibe/data
	mv modbus_addresses_all_20240903-06571123352007-1.csv s1256.csv
	cd ~/prj/nibe
	conda activate py312
	pip install -r requirements.txt
	python3 -m nibe.console_scripts.convert_csv
	python3 ./convert-s1256-to-yaml.py


.. code-block:: python
	:caption: ./convert-s1256-to-yaml.py

	import json
	import yaml

	# Pfade zu den Dateien
	json_dateipfad = 'nibe/data/s1256.json'
	yaml_dateipfad = 'nibe/data/s1256-config-coils.yaml'

	# Funktion zum Extrahieren der Werte aus den "name"-Tags
	def extrahiere_name_werte(json_daten):
		werte = [eintrag["name"] for eintrag in json_daten.values() if "name" in eintrag]
		return werte

	# JSON-Datei einlesen
	with open(json_dateipfad, 'r', encoding='utf-8') as json_datei:
		json_daten = json.load(json_datei)

	# Werte extrahieren
	werte = extrahiere_name_werte(json_daten)

	# YAML-Datei schreiben
	with open(yaml_dateipfad, 'w', encoding='utf-8') as yaml_datei:
		yaml.dump(werte, yaml_datei, default_flow_style=False, sort_keys=False)

	print(f'Werte wurden in die Datei {yaml_dateipfad} geschrieben.')


Konfiguration und Start des MQTT Servers
========================================

Die Ausgabe wird in die Datei :file:`~/prj/nibe-mqtt/config.yaml` in der Rubrik ``coils:`` eingetragen und der Docker Container mit dieser Konfiguration gestartet. Einige Werte müssen noch auskommentiert wernden, da sie für Fehlermeldungen beim Start oder WARNINGs während der Ausführung führen.

.. code-block:: bash

	docker run -ti --name nibe-mqtt --pull=always --rm -p 9999:9999/udp -v "/home/rainerth/prj/nibe-mqtt/config.yaml:/config/nibe-mqtt/config.yaml:ro" yozik04/nibe-mqtt:latest

