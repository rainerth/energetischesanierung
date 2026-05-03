#######################
Anfragen an den Support
#######################


OpenWB
======

Die per MQTT via mosquitto eingetragenen Werte für den Deye WR (``openWB/set/pv/8/get/power``) und die Deye Batterie (``openWB/set/bat/7/get/power``) springen mit jedem Messintervall von 0 auf einen plausiblen Wert.

.. code::

	MQTT Explorer openWB/set/pv/8/get/power:
	28.08.2024 11:32:13
	{}
	28.08.2024 11:32:13(-0.01 seconds)
	-4638

Im Diagramm sehe ich für die beiden Deye im 5 Minuten-Takt oszillierende Werte mit 0 und 5 Minuten später der doppelte erwartet Wert (~ 9,2kW). Bild dazu folgt per Mail.

.. figure:: ./images/oszillierende-deye-werte.png

