############################################
Die Raumtemperatur beeinflussen
############################################

Dieser Abschnitt beschreibt, welche Stellgrößen die Raumtemperatur in dieser Anlage tatsächlich verändern, welche Register dazugehören und welche Stolperstellen es gibt. Die Angaben sind entweder aus dem Herstellerhandbuch belegt oder an der Anlage gemessen; gemessene Aussagen sind als solche gekennzeichnet.


Wer bestimmt die Temperatur im Haus
===================================

Die Anlage hat drei Klimatisierungssysteme, aber nur zwei Verbraucherkreise. Das ist der Schlüssel zum Verständnis:

.. list-table::
	:header-rows: 1
	:stub-columns: 1

	*	-	System
		-	daran hängt
		-	Stellglied

	*	-	CS1
		-	**kein Verbraucher**. CS1 ist die Führungsgröße für die Puffertemperatur
		-	die Wärmeerzeugung selbst

	*	-	CS2
		-	Fußbodenheizung, 16 Kreise in EG und UG, über EP21
		-	Mischventil, regelt den eigenen Vorlauf

	*	-	CS3
		-	Heizkörper im Obergeschoss, über EP22
		-	keines, bekommt Puffertemperatur

.. admonition:: Gemessen am 20.10.2026

	Die Wärmeerzeugung folgt **ausschließlich** CS1. Die Gradminuten, also der Integrator, der den Verdichter startet und stoppt, werden aus der Abweichung zwischen dem externen Vorlauffühler ``BT25`` und dem Sollwert von CS1 gebildet:

	.. math::

		\frac{\mathrm{d}\,GM}{\mathrm{d}t} = T_{\mathrm{BT25}} - T_{\mathrm{Soll,CS1}}

	Geprüft über 563 Minutenschritte: Korrelation 0,975, Steigung 1,05, ein Kelvin Abweichung ergibt eine Gradminute pro Minute. Die Gegenkandidaten scheiden deutlich aus. Für CS2 wäre die mittlere Abweichung −5,7 K gewesen, die Gradminuten hätten um etwa 340 pro Stunde fallen müssen, tatsächlich lagen sie bei −6. Auch das Maximum über alle Klimatisierungssysteme scheidet aus: **die Anlage bildet kein Maximum.** Und maßgeblich ist ``BT25`` hinter dem Puffer, nicht ``BT2`` am Wärmepumpenausgang, dessen Korrelation sogar negativ ist.

	Es gibt überdies nur **einen** Gradminutenwert für die ganze Anlage (``vid 781``, Holding 40940 im Lesepfad ``degree-minutes-40012``), nicht einen pro System.

Daraus folgt die Reihenfolge, in der die Stellgrößen wirken:

#. **CS1** legt fest, wie warm der Puffer wird. Das wirkt auf **beide** Kreise.
#. **CS2** kann davon für die Fußbodenheizung nach unten abweichen, solange sein Sollwert **unter** der Puffertemperatur liegt.
#. **CS3** kann nicht abweichen.

.. attention::

	Liegt der Sollwert von CS2 **über** der Puffertemperatur, steht sein Mischventil dauerhaft offen und die Fußbodenheizung läuft auf Puffertemperatur. Kurve und Offset von CS2 sind dann **ohne jede Wirkung**. Ein Mischventil kann nur beimischen, also absenken, niemals anheben. Dieser Zustand ist von außen leicht zu übersehen, weil alle Parameter plausibel aussehen und sich beim Verstellen nichts ändert.

	Erkennen lässt er sich am Mischerhub, also der Differenz zwischen Puffertemperatur und Vorlauf hinter dem Mischventil. Liegt er in der Größenordnung des Leitungsverlusts, regelt nichts mehr.


Die Register je Klimatisierungssystem
=====================================

Modbus-Adressen in der 1-basierten Schreibweise, wie sie die NIBE-Dokumentation verwendet: Holding-Register ``40001 + ID``, Input-Register ``30001 + ID``. Die ``vid`` ist die Variablennummer, die das Display und die lokale REST-Schnittstelle verwenden.

.. list-table:: Einstellgrößen, alle schreibbar
	:header-rows: 1
	:stub-columns: 1

	*	-	Größe
		-	CS1
		-	CS2
		-	CS3
		-	Bereich

	*	-	Heizkurve
		-	40027
		-	40026
		-	40025
		-	0 bis 15

	*	-	Heizungsoffset
		-	40031
		-	**nicht verfügbar**
		-	40029
		-	−10 bis 10

	*	-	Min. Vorlauf Heizung
		-	40035
		-	40034
		-	40033
		-	5,0 bis 80,0 °C

	*	-	Max. Vorlauf Heizung
		-	40039
		-	40038
		-	40037
		-	5,0 bis 80,0 °C

	*	-	Raumfühler verwenden
		-	40203
		-	40202
		-	40201
		-	0 oder 1

	*	-	Raumsollwert
		-	40207
		-	40206
		-	40205
		-	5,0 bis 30,0 °C

	*	-	Raumfühlerfaktor
		-	40211
		-	40210
		-	40209
		-	0,0 bis 6,0

	*	-	externe Verstellung
		-	40052
		-	40051
		-	40050
		-	−10 bis 10

.. list-table:: Lesegrößen
	:header-rows: 1
	:stub-columns: 1

	*	-	Größe
		-	CS1
		-	CS2
		-	CS3

	*	-	berechneter Vorlauf
		-	31018
		-	31017
		-	31016

.. important::

	**Für CS2 gibt es keinen Heizungsoffset über Modbus.** Nach dem Registermuster müsste er auf Holding 40030 liegen, zwischen CS3 auf 40029 und CS1 auf 40031, und die Bibliothek ``yozik04/nibe`` führt ihn auch unter diesem Namen. Das Gerät antwortet darauf aber mit einer Modbus-Ausnahme, und in der lokalen REST-Schnittstelle fehlt die zugehörige ``vid`` ebenfalls. Bei Min- und Max-Vorlauf sind demgegenüber alle drei Systeme vorhanden.

	Der Offset für CS2 ist nur über das Display oder über myUplink erreichbar. **Die Cloud-Anbindung kann hier mehr als die lokale Schnittstelle.** Wer ausschließlich über Modbus arbeitet, kann diesen Wert weder lesen noch setzen und auch nicht prüfen, ob eine Änderung angekommen ist.


Der empfohlene Weg: der Offset
==============================

Für eine Korrektur der Raumtemperatur ist der Offset das vorgesehene Mittel, nicht die Vorlaufgrenze. Das Installateurhandbuch beschreibt in Menü 1.1.1 für den Betrieb ohne aktivierten Raumfühler:

.. epigraph::

	Einstellbereich: -10 – 10

	Das Display zeigt den eingestellten Wert für die Heizung (Parallelverschiebung). Um die Innenraumtemperatur anzuheben oder abzusenken, erhöhen bzw. verringern Sie den Wert im Display. Die Anzahl der Stufen, um die der Wert geändert werden muss, damit eine Änderung der Innenraumtemperatur um ein Grad erreicht wird, richtet sich nach Ihrem Klimatisierungssystem. Normalerweise genügt eine Stufe. In bestimmten Fällen können jedoch mehrere Stufen erforderlich sein.

	-- NIBE S1256 Installateurhandbuch, Menü 1.1.1

Die Einstellung erfolgt je Klimatisierungssystem. Als Richtgröße gilt also: **eine Stufe entspricht etwa einem Kelvin Raumtemperatur.**

.. hint::

	Die Anzeige wechselt die Einheit, wenn ein Raumfühler installiert und aktiviert ist. Dann stellt man in Menü 1.1.1 eine Solltemperatur zwischen 5 und 30 °C ein. Ohne aktivierten Raumfühler ist der Wert eine dimensionslose Parallelverschiebung zwischen −10 und 10.

Eine Senkung der **Kurvennummer** ist für eine Korrektur in der Übergangszeit das falsche Werkzeug. Die Kurven laufen bei milder Witterung zusammen und spreizen erst bei Kälte auf. Eine flachere Kurve senkt deshalb vor allem dort, wo die Wärme gebraucht wird, und kaum dort, wo es zu warm ist. Der Offset verschiebt dagegen parallel über den ganzen Bereich.


Vorlaufgrenzen sind keine Einstellparameter
===========================================

``Min. Vorlauf`` und ``Max. Vorlauf`` begrenzen den berechneten Sollwert nach unten beziehungsweise oben. Sie sind Grenzen, keine Regelgrößen, und wirken deshalb nur zeitweise.

.. admonition:: Gemessen am 20.10.2026

	Bei einer Min-Vorlaufgrenze von 28,0 °C auf CS1 lag der Sollwert in **46 Prozent** der Messpunkte exakt auf dieser Grenze, war also begrenzt. In den übrigen 54 Prozent lag er im Mittel 2,6 K darüber. Eine Absenkung der Grenze wirkt daher nur in knapp der Hälfte der Zeit, ein Offset dagegen immer.

	Ein Testlauf hat zusätzlich gezeigt, wie weit die Grenze eingreift: bei 7,7 °C Außentemperatur rechnete die Kurve für CS1 und CS3 je **25,9 °C**, die Grenze hob den Sollwert also um 2,1 K an.


Stolperstellen
==============

Der berechnete Vorlauf ist rampenbegrenzt
-----------------------------------------

.. admonition:: Gemessen am 20.10.2026

	Nach einer Änderung an Kurve, Offset oder Vorlaufgrenze ändert sich der angezeigte Sollwert **nicht sofort**. In einem Test blieb der Wert nach dem Anheben einer Max-Vorlaufgrenze rund acht Minuten unverändert und stieg danach mit etwa 0,04 K pro Minute auf das neue Niveau.

	Wer zwei Minuten nach einer Änderung nachsieht und keine Wirkung findet, schließt daraus leicht fälschlich, die Änderung sei nicht angekommen.

Eine Grenze kann die Messgröße verdecken
----------------------------------------

Steht der berechnete Sollwert an einer Vorlaufgrenze, ist er für die Diagnose unbrauchbar: jede Änderung einer anderen Stellgröße wird abgeschnitten und bleibt unsichtbar. Vor einem Test an Kurve oder Offset lohnt es sich zu prüfen, ob der Sollwert gerade an einer Grenze klebt.

Die externe Verstellung braucht einen AUX-Eingang
-------------------------------------------------

Die Register der externen Verstellung (40050 bis 40052) sind beschreibbar, wirken aber nur, wenn ein AUX-Eingang auf die Funktion ``Activate external adjustment`` konfiguriert ist. Ohne diese Zuordnung bleibt der Wert ohne Folge. Der wirksame Wert lässt sich an den zugehörigen Input-Registern kontrollieren.

Ein Raumfühler verändert die Regelstruktur
------------------------------------------

Mit ``Raumfühler verwenden`` = 1 korrigiert die Anlage den berechneten Vorlauf anhand der Abweichung zwischen Raumsollwert und gemessener Raumtemperatur, gewichtet mit dem Raumfühlerfaktor. Das Handbuch warnt ausdrücklich:

.. epigraph::

	Ein träges Heizsystem, wie z.B. eine Fußbodenheizung, kann für eine Steuerung per Raumfühler ungeeignet sein.

	-- NIBE S1256 Installateurhandbuch, Menü 1.3

Ein zweiter Hinweis betrifft die Platzierung: steht der Raumfühler in einem Raum mit Fußbodenheizung, soll er laut Handbuch nur anzeigen und nicht regeln.

.. attention::

	Wird der Raumfühler abgeschaltet, verliert ein gemischter Kreis seine raumbezogene Korrektur und regelt nur noch auf seine Kurve. Fällt dadurch der Sollwert über die Puffertemperatur, geht zugleich die Mischerregelung verloren, ohne dass sich der Vorlauf im ersten Moment ändert. Der Vorlauf bleibt zunächst gleich, der Regelweg ist aber ein anderer. Ein unveränderter Messwert heißt nicht, dass die Regelung unverändert arbeitet.


Vorgehen bei zu warmen Räumen
=============================

#. **Prüfen, welcher Kreis die Räume tatsächlich versorgt.** Bei einer Mischanlage ist das nicht zwangsläufig der Kreis, dessen Nummer zu den Räumen passt.
#. **Mischerhub messen.** Ist er in der Größenordnung des Leitungsverlusts, regelt der gemischte Kreis nicht, und sein Offset ist wirkungslos. Dann wirkt nur CS1.
#. **Prüfen, ob der Sollwert an einer Vorlaufgrenze klebt.** Wenn ja, zuerst die Grenze lösen, sonst ist jede weitere Messung blind.
#. **Offset in Einzelschritten ändern**, Richtgröße eine Stufe je Kelvin.
#. **Drei bis fünf Tage warten.** Ein Estrich reagiert träge; wer nach einem Tag nachjustiert, regelt gegen die Trägheit.
#. **Heizkörperkreise im Auge behalten.** Ein Heizkörper gibt bei niedriger Puffertemperatur kaum noch Leistung ab. Wo Fußbodenheizung und Heizkörper am gleichen Puffer hängen, begrenzen die Heizkörper, wie weit man gehen kann.
