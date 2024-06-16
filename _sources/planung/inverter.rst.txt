

Wechselrichter
==============

DEYE SUN-12K-SG04LP3-EU / Wifi
------------------------------

3-phasiger Hybrid-Wechselrichter. Interessant, da der bestehende Wechselrichter am Generatoreingang angeschlossen werden kann. Die Nord-PV-Anlage kann dann vermutlich an den PV-Eingang ran, mehr als 12kW sind da nicht zu erwarten.

.. seealso::

	* https://www.youtube.com/watch?v=i1oa_EbWJPI
	* https://www.youtube.com/watch?v=Hj5VTs9gGPg
	* `Deye Benutzerhandbuch <https://de.deyeinverter.com/deyeinverter/2023/03/24/rand/9271/%E3%80%90B%E3%80%91%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E%E4%B9%A6-%E5%82%A8%E8%83%BD%E4%B8%89%E7%9B%B8-SUN-(5-12)K-SG04LP3-EU-%E5%BE%B7%E4%B8%9A%E5%BE%B7%E8%AF%AD.pdf>`_



.. figure:: images/deye-wr-integration.png
   :alt: DEYE SUN-12K-SG04LP3-EU / Wifi
   :align: center

   DEYE SUN-12K-SG04LP3-EU / Wifi



Arbeitsmodus des Wechselrichters
--------------------------------

Verkauf zuerst:
	Die PV-Energie wird zur Versorgung der Last und zum Aufladen der Batterie verwendet. Überschüssige Energie wird in das Netz eingespeist.

	Die Priorität der Stromquelle für die Last ist: 1. Solarmodule, 2. Netz, 3. Batterie.


Null-Export zur Last:
	Der Wechselrichter versorgt nur die angeschlossene Ersatzlast mit Strom.

Null-Export an CT:
	Der Wechselrichter versorgt nicht nur die angeschlossene Haushaltslast mit Strom. Wenn die PV-Leistung und die Batterieleistung nicht ausreichen, wird die Energie des Netzes als Ergänzung genutzt. **Der Wechselrichter gibt keinen Strom an das Netz ab.**
