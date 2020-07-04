# coding: utf-8
from __future__ import print_function
from qgis.gui import QgsColorWidget

color_widget = QgsColorWidget(
    None,
    QgsColorWidget.Multiple  # Can be Multiple, Red, Green, Blue, Hue, Saturation, Value, Alpha
)
# fix_print_with_import

# fix_print_with_import
print((
    color_widget.color().red(),
    color_widget.color().green(),
    color_widget.color().blue()
))
print(color_widget.component())
print(color_widget.componentValue())

color_widget.show()
