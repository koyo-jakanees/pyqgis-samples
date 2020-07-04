# coding: utf-8
from __future__ import print_function
from qgis.PyQt.QtCore import QSettings
from qgis.core import QgsApplication
from qgis.gui import QgsSVGFillSymbolLayerWidget
from qgis.utils import iface

layer = iface.activeLayer()

# Print the SVG paths
print(QgsApplication.svgPaths())

# Specific to our use case.
# QgsApplication.setDefaultSvgPaths did not alter all the paths.
# Default value for "svg/searchPathsForSVG" is $HOME but as we had many git
# repositories under $HOME, QGIS was scanning all of them to look for SVG.
# Uncomment or not depending of your case
# s = QSettings()
# s.setValue("svg/searchPathsForSVG", "/tmp")  # Change the path if on Windows

# To confirm the difference if you apply above two previous lines
print(QgsApplication.svgPaths())

svg_fill_symbol_layer_widget = QgsSVGFillSymbolLayerWidget(
    layer
)
svg_fill_symbol_layer_widget.show()
