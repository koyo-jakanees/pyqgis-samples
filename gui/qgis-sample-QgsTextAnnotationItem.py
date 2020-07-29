# coding: utf-8
from qgis.PyQt.QtCore import QSizeF
from qgis.PyQt.QtGui import QColor, QTextDocument
from qgis.core import QgsPointXY, QgsTextAnnotation

# from qgis.gui import
from qgis.utils import iface

canvas = iface.mapCanvas()
crs = QgsCoordinateReferenceSystem("EPSG:4326")
text_annotation = QgsTextAnnotation(canvas)
X, Y = float(37.0), float(0.1)
point = QgsPointXY(X, Y)
text_annotation.setMapLayer(iface.activeLayer())
text_annotation.setMapPositionCrs(crs)
text_annotation.setMapPosition(point)
text_annotation.setFrameSize(QSizeF(300, 200))
# text_annotation.setFrameColor(QColor(0, 255, 0))
# text_annotation.setFrameBackgroundColor(QColor(128, 128, 128))
text_document = QTextDocument()
html_content = "<b>New annotation</b>"
font_color, font_family, font_size = "#123456", "Times New Roman", 16
text_document.setHtml(
    '<font style="color:'
    + font_color
    + "; font-family:"
    + font_family
    + "; font-size: "
    + str(font_size)
    + 'px">'
    + html_content
    + "</font>"
)
text_annotation.setDocument(text_document)
text_annotation.setVisible(True)
print(text_annotation.mapPositionCrs())
canvas.refresh()

# Then remove
# canvas.scene().removeItem(text_annotation_item)
