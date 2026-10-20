#########################################
Einspeisung ins öffentliche und Hausnetz
#########################################


Die elektrische Verschaltung von einem System mit 2 Wechselrichtern mit 2 PV-Anlagen und einer Batterie ist genau zu planen. Wie kann ich also den Strom der PV-Anlage 1 mit Wechselrichter 1 mit dem Hausnetz verbinden und den Strom ins öffentliche Netz einspeisen und den Strom des Wechselrichter 2 von PV-Anlage 2 verwenden um die Batterie aufzuladen und ins Hausnetz einspeisen - aber nicht ins öffentliche Netz?

Hier skizziere ich eine mögliche Lösung, wie man die verschiedenen Energieflüsse steuern kann:

Grundlegendes Schaltungslayout
==============================

1. **PV-Anlage 1 und Wechselrichter 1:**

   - Diese Anlage ist für die direkte Versorgung des Hausnetzes und die Einspeisung des überschüssigen Stroms ins öffentliche Netz zuständig.

   - Der Wechselrichter sollte ans Hausnetz angeschlossen werden, mit der Option, überschüssige Energie ins öffentliche Netz zu leiten.

2. **PV-Anlage 2 und Wechselrichter 2:**

   - Dieser Wechselrichter wird speziell für das Laden der Batterie und die Versorgung des Hausnetzes genutzt, jedoch ohne Einspeisung ins öffentliche Netz.

   - Der Wechselrichter benötigt eine direkte Verbindung zur Batterie und eine Möglichkeit, die Energie ins Hausnetz zu leiten.

Technische Implementierung
==========================

- **Bidirektionale Wechselrichter für Wechselrichter 2:**

  - Verwenden Sie einen bidirektionalen Wechselrichter (auch als Hybridwechselrichter bekannt), der sowohl die Batterie laden als auch das Hausnetz versorgen kann. Dieser Wechselrichter kann auch sicherstellen, dass keine Energie ins öffentliche Netz fließt.

- **Energie-Management-System (EMS):**

  - Ein EMS ist entscheidend, um die Energieflüsse intelligent zu steuern und zu überwachen.

  - Es kann zwischen den beiden Wechselrichtern koordinieren, entscheiden, wann die Batterie geladen wird, und sicherstellen, dass die Energieverwendung im Haus optimiert wird.

  - Es verhindert auch, dass Energie von Wechselrichter 2 ins öffentliche Netz eingespeist wird, indem es nur die notwendige Energie ins Hausnetz leitet und Überschüsse zur Batterieladung verwendet.

- **Netztrennschalter und Schutzmaßnahmen:**

  - Installieren Sie geeignete Schalter und Relais, um physikalisch sicherzustellen, dass keine Energie von Wechselrichter 2 ins öffentliche Netz fließt.

  - Sicherheitsvorrichtungen und Schutzeinrichtungen (z.B. Überlastschutz, Rückspeisungsschutz) sind erforderlich, um sowohl das öffentliche Netz als auch Ihr Hausnetz zu schützen.

- **Verkabelung und Sicherungen:**

  - Stellen Sie sicher, dass die Verkabelung und die Sicherungen entsprechend der maximalen Leistung und den Stromstärken der Wechselrichter und der Batterie ausgelegt sind.

  - Achten Sie darauf, dass alle Verbindungen korrekt isoliert und sicher installiert sind.

Zusätzliche Überlegungen
========================

- **Regulatorische und Netzbedingungen:** Prüfen Sie die lokalen Vorschriften bezüglich der Einspeisung in das öffentliche Netz und der Nutzung von Stromspeichern.

- **Wartung und Überwachung:** Planen Sie regelmäßige Wartungen ein, und setzen Sie möglicherweise Überwachungssysteme ein, um die Performance des Systems und den Zustand der Batterie zu überwachen.

Diese Konfiguration erfordert eine sorgfältige Planung und oft auch die Zusammenarbeit mit einem Fachbetrieb, der Erfahrung mit der Installation und Konfiguration von hybrid PV- und Speichersystemen hat. Es ist auch ratsam, mit dem lokalen Energieversorger und/oder Netzwerkbetreiber zusammenzuarbeiten, um alle Anforderungen und Vorschriften zu erfüllen.


Netzdienlichkeit
================

Die Festlegungen der BNetzA zu§14a EnWG ab 1. Januar 2024 im Überblick:

Die Teilnahme von steuerbaren Verbrauchseinrichtungen mit einer Bezugsleistung von mehr als 4,2 kW am neuen §14 a-Modell ist verpflichtend, wenn diese ab dem 01.01.2024 in Betrieb genommen wurden

Einführung von 3 neuen Netzentgeltmodulen, die eine Reduzierung der Netzentgelte vorsehen.

Ein separater Zähler für einen steuerbaren Verbraucher ist keine zwingende Voraussetzung mehr für die Teilnahme an §14a EnWG.

.. seealso:: 
	
	* `§14a EnWG <https://enbw-eg.de/blog/14a-enwg-neuregelung>`_
	* :download:`Funkrundsteuerung in EEG-Anlagen </_static/datenblaetter/eeg-fre-montageanleitung.pdf>`
	* `OpenWB Forum: Steuerbare Verbrauchseinrichtung §14 EnWG <https://forum.openwb.de/viewtopic.php?t=8019&start=100>`_




.. epigraph:: 
	
	Netze-BW: 
	
	Leider geht es bei einer gemeinsamen Messung mit 2 PV-Anlagen nicht, ein intelligentes Messsystem einzubauen, wegen der Abrechnung.


Messkonzept
===========

.. figure:: ./images/pv-autark-MK40-V2.png

FRE Rundsteuerempfänger
-----------------------

.. figure:: ./images/eeg-rundsteuerempfaenger.png


OpenWB Dimm- und Control-Kit
----------------------------

.. figure:: ./images/openWBDimm-ControlModul-v1.png

Das openWB "Dimm- & Control-Kit" ermöglicht die Auswertung von bis zu 8 Steuersignalen des Energieversorgers mittels potentialfreier Kontakte aus dessen :download:`Rundsteuerempfänger (RSE, FRE) </_static/datenblaetter/eeg-fre-montageanleitung.pdf>` bzw. Steuerbox (z.B. nach §14a EnWG).

Die Eingangssignale werden im Kit zu Netzwerksignalen übersetzt und dem openWB-Energiemanagementsystem (EMS) bzw. Lastmanagement (LM) zur weiteren Verarbeitung zur Verfügung gestellt. Die Eingangssignale können für eine reduzierte als auch komplette Abschaltung der Ladevorgänge sowie weiterer steuerbarer Verbraucher (StVE) genutzt werden (gesamtheitliche Steuerung über das openWB-EMS/LM).

Gleichzeitig bietet das “Dimm- & Control-Kit” 8 Relaisausgänge zur direkten Kontrolle steuerbarer Verbraucher (StVE). Die Ausgänge sind potentialfrei als NO/NC ausgeführt und mit bis zu 5A@28VDC/250VAC belastbar.
Hiermit lassen sich z. B. einzelne Verbraucher situationsbedingt schalten bzw. dimmen. Hierzu zählen auch “SG-Ready”-Kontakte (und Vergleichbare) von Wärmepumpen oder anderen Verbrauchern.*

Die Möglichkeiten der Ein-/Ausgänge werden in openWB Software (ab software2) konfiguriert.

Zusätzlich verfügt das “Dimm- & Control-Kit” über eine Heartbeat-Funktionalität zur Eigenüberwachung. Gibt es Netzwerkstörungen oder Kommunikationsprobleme, so wird eine konfigurierbare “Dimmung” der Verbraucher über die openWB-Software vorgenommen, um Überlastungen sicher zu verhindern.
Ggf. genutzte Ausgänge des Kits schalten in diesem Fall angeschlossene Verbraucher automatisch ab.

Das openWB “Dimm- & Control-Kit” kann sowohl auf Hutschiene als auch per Wandmontage bestellt werden. Je nach Auswahl erfolgt die Lieferung mit Hutschienen- oder Steckernetzteil und entsprechendem Befestigungsmaterial. Der Anschluss erfolgt über Netzwerk (LAN).

Zur Nutzung wird eine openWB (alle Varianten möglich) mit mind. software2 benötigt. Unabhängig von der Anzahl der Ladepunkte ist nur ein “Dimm- & Control-Kit” erforderlich.
Der max. Leitungsweg der potentialfrei geschaltenen Eingänge ist auf 2 m ausgelegt. Die Ausgänge werden im Normalfall spannungsführend genutzt, so dass die Leitungslängen entsprechend den gültigen VDE-Vorschriften nutzbar sind.

.. hint:: 
	Die Ausgänge sind zum Zeitpunkt der Auslieferung noch nicht in der Software2 implementiert. Das Feature wird per Update nachgereicht


