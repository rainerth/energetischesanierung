######################
Anmeldung der Anlagen
######################

Die PV Anlage muss vor Inbetriebnahme bei Netze-BW angemeldet werden. Die Anmeldung erfolgt über das Online-Portal der Netze-BW. Die Anmeldung ist kostenfrei.


1. Ermittlung der Gesamtleistung der PV-Module
==============================================

Zuerst müssen Sie die Gesamtleistung der PV-Module, die an den Wechselrichter angeschlossen werden sollen, berechnen. Dies errechnet sich üblicherweise durch Multiplikation der Anzahl der Module mit der Nennleistung eines jeden Moduls:

.. epigraph::

	P\ :sub:`total` = n × P\ :sub:`modul`

wo n die Anzahl der Module und P\ :sub:`modul` die Nennleistung eines Moduls in Watt ist.

.. epigraph::

	P\ :sub:`total` = 56 x 330W = 18480W = 18,48kW


2. Berücksichtigung der PV-Modul-Leistungstoleranz
==================================================

Die tatsächliche Leistung der PV-Module kann aufgrund von Leistungstoleranzen variieren. Meist liegt die Toleranz im Bereich von -0% bis +5%. Es ist ratsam, die maximale Leistung zu berücksichtigen, um sicherzustellen, dass der Wechselrichter auch bei höherer Modulleistung angemessen funktioniert.

Die Leistungstoleranz der Heckert 330 W Module beträgt `0 / +4,99 Wp`. Die maximale Leistung der Module beträgt daher 330 + 4,99 = 334,99 Wp.

.. epigraph::

	P\ :sub:`total` = 56 x 334,99W = 18747,44W = 18,75kW


3. Wahl der Wechselrichterleistung
==================================

Der Wechselrichter sollte so gewählt werden, dass seine Nennleistung die Spitzenleistung der PV-Module aufnehmen kann, aber nicht zu groß dimensioniert ist, da dies zu einer ineffizienten Betriebsweise führen kann. Die Leistung des Wechselrichters sollte daher in etwa der maximalen Leistung der PV-Module entsprechen oder diese leicht übersteigen.



4. Überlegungen zur Umrichterscheinleistung

Die **Scheinleistung** `S` eines Wechselrichters ist durch seine Fähigkeit bestimmt, **Wirkleistung** und **Blindleistung** zu handhaben. Sie wird normalerweise in **Voltampere (VA)** angegeben und ergibt sich aus der Formel:

.. epigraph::

	S = V × I

wo `V` die Spannung und `I` der Strom ist. Bei der Auswahl eines Wechselrichters muss darauf geachtet werden, dass die Scheinleistung mindestens so hoch ist wie die Gesamtleistung der PV-Module, die in Watt (W) gemessen wird, um sowohl die Wirk- als auch die Blindleistungsanforderungen zu erfüllen.


5. Einbeziehung von Umweltfaktoren
==================================

Für eine PV-Anlage mit der Ausrichtung Nord und einer Dachneigung von 30 Grad in Deutschland kann von einer Reduktion der Gesamtleistung auf 60,5% ausgegangen werden. Dies bedeutet, dass die tatsächliche Leistung der PV-Module bei diesen Bedingungen 60.5% der Nennleistung beträgt.

.. admonition:: Quelle

	https://photovoltaik.org/solarstrom/solarenergie/neigungswinkel

.. epigraph::

	P\ :sub:`total` = 56 x 334,99W * 0,6050 = 11352,47W = 11,35kW





Leistungsangaben der Erzeugungsanlage(n)
Geplante (Modul-) Leistung PAGen (Summenleistung aller Module)


Bemessungsscheinleistung aller geplanten Erzeugungseinheiten (Umrichterscheinleistung) ΣS r,E

Die Bemessungsscheinleistung aller geplanten Erzeugungseinheiten (Umrichterscheinleistung) ΣS r,E beträgt 10 kW.

Maximale Wirkleistung aller geplanten Erzeugungseinheiten (Umrichterwirkleistung) ΣP Emax


Anschlusswirkleistung der existierenden Anlage


[X] Es ist ein Speichersystem geplant:
Maximale Wirkleistung aller geplanten Speicher ΣPEmax