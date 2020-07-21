# coding: utf-8
from __future__ import print_function
from qgis.PyQt.QtWidgets import QDialog
from qgis.core import QgsStyle, QgsColorRamp
from qgis.gui import QgsColorRampButton # replaces QgsColorRampComboBox

# Create dialog and resize it
new_dialog = QDialog()
new_dialog.resize(800, 600)

# style = QgsStyle().defaultStyle() API3 no longer uses the defualt QgsStyle

color_ramp_combo_box = QgsColorRampButton(new_dialog)
color_ramp_combo_box.setToDefaultColorRamp() 
# accepts '.setRandomColorRamp(), .setToDefaultColorRamp(), .setToNull()'


def on_color_ramp_changed():
    print(color_ramp_combo_box.colorRamp())
    print(color_ramp_combo_box.colorRampName())
    print("Color ramp changed")

color_ramp_combo_box.colorRampChanged.connect(on_color_ramp_changed)

new_dialog.show()
