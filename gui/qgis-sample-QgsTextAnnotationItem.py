# coding: utf-8
from qgis.PyQt.QtCore import QSizeF
from qgis.PyQt.QtGui import QColor, QTextDocument
from qgis.core import QgsPointXY, QgsTextAnnotation, QgsProject

from qgis.gui import QgsMapCanvasAnnotationItem
from qgis.utils import iface

canvas = iface.mapCanvas()
text_annotation = QgsTextAnnotation(canvas)
X, Y = float(37.0), float(-1.1)
point = QgsPointXY(X, Y)
text_annotation.setMapLayer(iface.activeLayer())
text_annotation.setMapPositionCrs(iface.activeLayer().crs())
text_annotation.setMapPosition(point)
text_annotation.setFrameSizeMm(QSizeF(50, 50))
#text_annotation.setFrameColor(QColor(0, 255, 0))
#text_annotation.setFillSymbol('Fill')
#text_annotation.setFrameBackgroundColor(QColor(128, 128, 128))
text_document = QTextDocument()
html_content = "<b>New annotation Now requires a \
QgsMapCanvasAnnotationItem: versionadded::3.0</b>"
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
w = QgsMapCanvasAnnotationItem(text_annotation, canvas) 
w.setOpacity(0.5)
canvas.refresh()

# Then remove
#canvas.scene().removeItem(w) 


#Experiment with this: causes qgis to crash
#QgsProject.instance().annotationManager().addAnnotation(text_annotation)

#Note: you can use either 
#https://gis.stackexchange.com/questions/282854/programatically-adding-annotations/323292
# 1. QgsProject.instance().annotationManager().addAnnotation(text_annotation) or
# 2. QgsMapCanvasAnnotationItem(text_annotation, canvas) to add the item
#TODO: used together with Map canvas Class```An interactive map canvas item which displays a QgsAnnotation.```
