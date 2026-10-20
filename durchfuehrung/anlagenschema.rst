##############
Anlagenschema
##############

Die beiden folgenden Schemata zeigen den tatsächlich gebauten Stand, nicht die Planung. Sie enthalten bewusst keine Momentanwerte, damit sie nicht veralten.

.. note::

	Beide Zeichnungen werden aus Graphviz-Quellen erzeugt, die im Repository liegen (:file:`durchfuehrung/diagramme/`). Änderungen am Schema gehören in die ``.dot``-Datei, nicht in ein Bildbearbeitungsprogramm.


Hydraulik
=========

.. graphviz:: diagramme/hydraulik.dot
	:caption: Hydraulikschema: Wärmequelle, Wärmepumpe, Kühlung, Puffer und die beiden Hauskreise

Der Aufbau hat eine Eigenheit, die für das Verständnis der Regelung entscheidend ist: **zwischen Wärmepumpe und Hauskreisen sitzt ein Pufferspeicher ACF 50 mit 50 Litern**. Der offizielle Hydraulikplan PL1.115, nach dem die Kühlfunktion gebaut wurde, sieht ihn nicht vor. Beide Hauskreise zweigen hinter diesem Puffer ab:

Klimatisierungssystem 2, Fußbodenheizung über EP21
	16 Heizkreise, zehn im Erdgeschoss und sechs im Untergeschoss. Dieser Kreis hat ein **Mischventil** und regelt seine Vorlauftemperatur selbst, indem er dem Puffer kälteres Rücklaufwasser beimischt.

Klimatisierungssystem 3, Heizkörper im Obergeschoss über EP22
	Dieser Kreis hat **kein Stellglied**. Er bekommt die Puffertemperatur, abzüglich des Leitungsverlusts.

Klimatisierungssystem 1
	Daran hängt **kein Verbraucher**. CS1 ist die Führungsgröße für die Temperatur im Puffer. Details in :doc:`raumtemperatur`.

.. attention::

	Ein Mischventil kann nur beimischen, also absenken. Fordert ein gemischter Kreis eine höhere Temperatur, als im Puffer steht, bleibt ihm nur, vollständig zu öffnen. Er bekommt dann Puffertemperatur, und seine eigene Heizkurve ist ohne Wirkung. NIBE formuliert das als Installationsvoraussetzung im Installateurhandbuch des AXC 30, Abschnitt „Rohranschluss / Allgemeines“:

	.. epigraph::

		Bei Anschluss zusätzlicher Klimatisierungssysteme müssen diese so eingebunden werden, dass sie eine niedrigere Betriebstemperatur als Klimatisierungssystem 1 besitzen.


Stromlauf
=========

.. graphviz:: diagramme/strom.dot
	:caption: Stromlaufschema: zwei Erzeugungsanlagen, vier Zähler, Speicher und die großen Verbraucher

Die Liegenschaft hat zwei Photovoltaikanlagen unterschiedlicher Generation und vier Zähler, die über IR-Leseköpfe ausgelesen werden.

.. list-table:: Zählerzuordnung
	:header-rows: 1
	:stub-columns: 1

	*	-	Zähler
		-	Messstelle
		-	Bedeutung

	*	-	Z1
		-	Hausanschluss
		-	bilanziert die ganze Liegenschaft, also auch Wärmepumpe und Wallbox

	*	-	Z2
		-	Unterzähler
		-	nur der Haushalt. Wärmepumpe und Wallbox liegen **außerhalb** von Z2

	*	-	Z3
		-	Ausgang Süd-Wechselrichter
		-	reiner Erzeuger

	*	-	Z4
		-	Ausgang Deye-Wechselrichter
		-	PV Nord, Batteriespeicher und Eigenbedarf des Wechselrichters zusammen

.. important::

	Weil Z1 die ganze Liegenschaft erfasst und Z2 nur den Haushalt, lässt sich der Autarkiegrad **nicht** als Verhältnis von Z2 zu Z1 berechnen. Die tragfähige Form ist

	.. math::

		\mathrm{Autarkie} = \frac{E_{\mathrm{Eigenverbrauch}}}{E_{\mathrm{Eigenverbrauch}} + E_{\mathrm{Z1,Bezug}}}
		\quad\text{mit}\quad
		E_{\mathrm{Eigenverbrauch}} = E_{\mathrm{PV,gesamt}} - E_{\mathrm{Z1,Einspeisung}}

.. list-table:: Erzeugungsanlagen
	:header-rows: 1
	:stub-columns: 1

	*	-
		-	PV Süd
		-	PV Nord

	*	-	Inbetriebnahme
		-	2019
		-	2024

	*	-	Generatorleistung
		-	12,6 kWp
		-	18,48 kWp

	*	-	Ausrichtung
		-	Süd, 30° Neigung
		-	Nord, 30° Neigung

	*	-	Module
		-	\-
		-	56 × Heckert Solar NEMO 2.0 60 M, 330 Wp

	*	-	Strings
		-	1 MPP-Tracker belegt von 2
		-	3 Strings: 19 / 19 / 18 Module

	*	-	Wechselrichter
		-	KACO blueplanet 15.0 TL3
		-	Deye SUN-12K-SG04LP3-EU, Hybrid

	*	-	Speicher
		-	\-
		-	LiFePO4 am Hybridwechselrichter

.. hint::

	Der zweite MPP-Tracker des Süd-Wechselrichters ist seit der Inbetriebnahme unbelegt, die gesamten 12,6 kWp hängen an DC1. Am offenen Eingang DC2 liegt eine Phantomspannung von rund 241 V bei 0 A. Das ist kein Defekt, war aber in der Diagnose zunächst irritierend.


Messpfad
========

Alle Energiedaten laufen über denselben Weg in die Zeitreihendatenbank. Die vier Zähler werden mit IR-Leseköpfen abgegriffen, Wärmepumpe und Wechselrichter über Modbus.

.. graphviz:: diagramme/messpfad.dot
	:caption: Vom Zähler bis ins Dashboard

Die Einzelheiten stehen in :doc:`energiezaehler`, :doc:`nibe-mqtt`, :doc:`deye-mqtt` und :doc:`telegraf-influxdb`.

.. warning::

	Die Vorzeichen sind zwischen den Quellen **nicht** einheitlich. Für die Batterieleistung gilt in der openWB-Konvention ein positives Vorzeichen beim Laden, in den rohen Modbus-Werten des Deye dagegen ein negatives. Wer beide Quellen in einer Auswertung mischt, muss eine davon invertieren, sonst heben sich Lade- und Entladeleistung scheinbar auf.
