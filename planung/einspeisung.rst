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