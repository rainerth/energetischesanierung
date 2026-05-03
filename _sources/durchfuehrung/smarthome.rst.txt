###########
Smart Home
###########


Setup mit FHEM, InfluxDB und Grafana
====================================

Eine existierende FHEM Installation soll um eine influxdb für Messwerte und Grafana zur Anzeige der Messwerte erweitern werden. Alternativ kann statt der influxdb auch mysql verwendet werden.

Was ist der Vorteil von influxdb gegenüber mysql in diesem Kontext?
-------------------------------------------------------------------

Der Vergleich zwischen InfluxDB und MySQL für das Speichern und Verwalten von Zeitreihendaten, wie sie bei FHEM-Messwerten anfallen, zeigt einige klare Vorteile von InfluxDB gegenüber MySQL in diesem speziellen Kontext:

Vorteile von InfluxDB gegenüber MySQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Optimierung für Zeitreihendaten**:
   - **InfluxDB**: Speziell für Zeitreihendaten entwickelt. Sie bietet native Unterstützung für Zeitstempel und ermöglicht effiziente Abfragen und Aggregationen von Zeitreihendaten. Dies umfasst schnelle Abfragen von Zeitbereichen, kontinuierliche Datenaggregation und Rollups.
   - **MySQL**: Obwohl MySQL Zeitstempel unterstützt, ist es nicht speziell für Zeitreihendaten optimiert. Es kann bei großen Mengen an Zeitreihendaten weniger effizient sein und zusätzliche Komplexität bei Abfragen und Aggregationen aufweisen.

2. **Einfache Verwaltung von großen Datenmengen**:
   - **InfluxDB**: Entwickelt, um große Mengen an Zeitreihendaten zu speichern und zu verwalten, einschließlich effizienter Komprimierung und Datenaufbewahrung (Retention Policies). Dies hilft dabei, alte Daten automatisch zu archivieren oder zu löschen.
   - **MySQL**: Bei großen Mengen an Zeitreihendaten kann MySQL in Bezug auf Speicherplatz und Performance problematisch werden, insbesondere bei Abfragen über große Zeiträume und beim Umgang mit sehr vielen Datensätzen.

3. **Abfrageoptimierung für Zeitreihendaten**:
   - **InfluxDB**: Bietet speziell optimierte Funktionen für Zeitreihendaten wie `GROUP BY time()`, `mean()`, `sum()`, und `derivative()`, die für typisches Monitoring und Aggregation nützlich sind.
   - **MySQL**: Muss für solche zeitbasierten Aggregationen und Berechnungen möglicherweise kompliziertere Abfragen oder zusätzliche Tabellenstrukturen verwenden, was die Performance beeinträchtigen kann.

4. **Retention Policies und Continuous Queries**:
   - **InfluxDB**: Unterstützt Retention Policies (Automatisches Löschen alter Daten) und Continuous Queries (Automatisches Aggregieren von Daten über Zeit), was die Verwaltung von Datenvolumen und die Berechnung von Metriken erleichtert.
   - **MySQL**: Solche Funktionen müssen manuell implementiert werden, was zusätzlichen Aufwand bei der Datenverwaltung bedeutet.

5. **Leistung und Skalierbarkeit**:
   - **InfluxDB**: Kann effizient mit sehr großen Datenmengen umgehen und bietet Funktionen zur Horizontalen Skalierung (in den Enterprise-Versionen), die für große und stark wachsende Datensätze von Vorteil sind.
   - **MySQL**: Skaliert gut, aber das Handling von sehr großen Zeitreihendatenmengen kann komplizierter sein und erfordert zusätzliche Optimierungen oder Partitionierungen.

6. **Schemafrei**:
   - **InfluxDB**: Erlaubt Schemafreiheit bei der Datenspeicherung, was die Flexibilität erhöht und die Notwendigkeit reduziert, das Schema im Voraus zu definieren oder anzupassen.
   - **MySQL**: Erfordert ein festgelegtes Schema, was die Flexibilität einschränken und zusätzliche Anpassungen bei Änderungen an den Datenstrukturen erfordern kann.

Zusammenfassung
~~~~~~~~~~~~~~~

- **InfluxDB** ist besonders vorteilhaft, wenn du mit großen Mengen von Zeitstempeldaten arbeitest, schnelle und effiziente Zeitreihendaten-Abfragen benötigst, und von Funktionen wie Retention Policies und Continuous Queries profitieren möchtest.
- **MySQL** ist ein bewährtes relationales Datenbankmanagementsystem, das ebenfalls Zeitstempeldaten verarbeiten kann, jedoch zusätzliche Komplexität und Aufwand für die Optimierung und Skalierung bei großen Zeitreihendatenmengen mit sich bringen kann.

Für Anwendungsfälle, bei denen die Hauptanforderung eine effiziente Verarbeitung und Analyse von Zeitreihendaten ist (wie bei der Überwachung und Analyse von FHEM-Messwerten), bietet InfluxDB klare Vorteile.


Installation von InfluxDB und Grafana per Docker
================================================

Die Installation von InfluxDB und Grafana per Docker kann eine sehr praktische und effiziente Methode sein, um diese Dienste zu betreiben. Docker bietet eine isolierte Umgebung für jede Anwendung, vereinfacht die Installation und Konfiguration und erleichtert die Verwaltung und Skalierung.

Hier ist eine Schritt-für-Schritt-Anleitung zur Installation von InfluxDB und Grafana per Docker:

**Vorbereitung**
	Stelle sicher, dass Docker und Docker Compose auf deinem System installiert sind. Falls nicht, kannst du sie wie folgt installieren:

**Docker installieren**::

  sudo apt update
  sudo apt install docker.io

**Docker Compose installieren**::

	sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep tag_name | cut -d '"' -f 4)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose

**Docker-Compose-Datei erstellen**
	Erstelle ein Verzeichnis für deine Docker-Compose-Konfiguration und eine `docker-compose.yml`-Datei:

**Erstelle das Verzeichnis**::

   mkdir -p ~/docker/influxdb-grafana
   cd ~/docker/influxdb-grafana

**Erstelle die `docker-compose.yml`-Datei**::

	version: '3'
	services:
		influxdb:
		image: influxdb:latest
		container_name: influxdb
		ports:
			- "8086:8086"
		volumes:
			- influxdb-data:/var/lib/influxdb
		networks:
			- monitoring

		grafana:
		image: grafana/grafana:latest
		container_name: grafana
		ports:
			- "3000:3000"
		depends_on:
			- influxdb
		networks:
			- monitoring

	volumes:
		influxdb-data:

	networks:
		monitoring:

**Dienste starten**
	Starte die Docker-Container mit Docker Compose::

		docker-compose up -d


Alternative::
	grafana läuft bereits als systemd Service. InfluxDB wird als Docker Container gestartet::

		docker run \
		--name influxdb2 \
		--publish 8086:8086 \
		--mount type=volume,source=influxdb2-data,target=/mnt/db/influx01 \
		--mount type=volume,source=influxdb2-config,target=/etc/influxdb2 \
		--env DOCKER_INFLUXDB_INIT_MODE=setup \
		--env DOCKER_INFLUXDB_INIT_USERNAME=admin \
		--env DOCKER_INFLUXDB_INIT_PASSWORD=dracha35 \
		--env DOCKER_INFLUXDB_INIT_ORG=DFVB \
		--env DOCKER_INFLUXDB_INIT_BUCKET=ogn \
		influxdb:2

Konfiguration der InfluxDB
--------------------------

**Erstelle eine Datenbank in InfluxDB**
   Du kannst dies mit dem `influx` CLI-Tool tun. Starte den InfluxDB-Container::

	   docker exec -it influxdb influx

   Dann führe die folgenden Befehle im InfluxDB-CLI aus:

   .. code-block:: sql

	CREATE DATABASE fhem
	CREATE USER "fhem_user" WITH PASSWORD 'your_password'
	GRANT ALL ON "fhem" TO "fhem_user"


Konfiguration von Grafana
-------------------------

**Öffne Grafana im Browser**:
   Gehe zu `http://localhost:3000`. Der Standardbenutzername und das Passwort sind `admin` und `admin`.

**Füge InfluxDB als Datenquelle hinzu**:
   - Melde dich bei Grafana an.
   - Gehe zu „Configuration“ (Zahnrad-Symbol) > „Data Sources“.
   - Klicke auf „Add data source“.
   - Wähle „InfluxDB“ aus.
   - Setze die URL auf `http://influxdb:8086` (Dies ist der Name des InfluxDB-Services im Docker-Netzwerk).
   - Setze den „Database“-Namen auf `fhem`.
   - Setze den „User“ und „Password“ auf die Anmeldedaten, die du in InfluxDB erstellt hast.
   - Klicke auf „Save & Test“.

**Erstelle Dashboards in Grafana**:
   - Gehe zu „Create“ (Plus-Symbol) \> „Dashboard“.
   - Füge Panels hinzu und konfiguriere sie, um Daten aus der InfluxDB anzuzeigen.

Zusammenfassung
---------------

- **Docker und Docker Compose** bieten eine einfache Möglichkeit, InfluxDB und Grafana zu installieren und zu verwalten.
- **`docker-compose.yml`** definiert die Konfiguration der beiden Container und sorgt für eine einfache Verwaltung.
- **InfluxDB** wird über Docker-Volumen persistent gehalten.
- **Grafana** wird über Docker-Compose verwaltet und startet nach InfluxDB.

Diese Methode ist besonders nützlich für Testumgebungen und kleinere Installationen. Für Produktionsumgebungen solltest du zusätzliche Überlegungen zu Datensicherung, Sicherheit und Skalierung einbeziehen.






https://github.com/tsunami42/tsm_restore?tab=readme-ov-file
