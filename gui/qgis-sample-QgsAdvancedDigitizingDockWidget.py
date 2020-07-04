# coding: utf-8
from __future__ import print_function
from qgis.PyQt.QtCore import Qt
from qgis.gui import QgsAdvancedDigitizingDockWidget
from qgis.utils import iface

canvas = iface.mapCanvas()
dock = QgsAdvancedDigitizingDockWidget(canvas)

iface.addDockWidget(Qt.RightDockWidgetArea, dock)

iface.removeDockWidget(dock)

# Access to the existing instance instead of the newly created one
print(iface.cadDockWidget())  # Return QGIS existing instance of QgsAdvancedDigitizingDockWidget
iface.cadDockWidget().show()
