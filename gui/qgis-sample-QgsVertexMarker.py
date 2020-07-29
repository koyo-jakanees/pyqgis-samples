# coding: utf-8
from qgis.PyQt.QtGui import QColor
from qgis.utils import iface
from qgis.core import QgsPointXY
from qgis.gui import QgsVertexMarker

canvas = iface.mapCanvas()
m = QgsVertexMarker(canvas)
m.setCenter(QgsPointXY(0, 0))

m.setColor(QColor(0, 0, 255))
m.setIconSize(7)
m.setIconType(QgsVertexMarker.ICON_BOX)  
# See the enum IconType from http://www.qgis.org/api/classQgsVertexMarker.html: 
# ICON_NONE, ICON_CROSS, ICON_CIRCLE, ICON_DOUBLE_TRIANGLE, ICON_RHOMBUS
m.setPenWidth(3)

m.hide()
m.show()

# Remove the element
# canvas.scene().removeItem(m)
