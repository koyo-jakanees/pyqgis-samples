# coding: utf-8
from __future__ import print_function
from qgis.gui import QgsColorWheel

color_wheel = QgsColorWheel()


def on_color_wheel_changed(color):
    print(color)

color_wheel.colorChanged.connect(on_color_wheel_changed)

color_wheel.show()
