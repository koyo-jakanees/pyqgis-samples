# coding:utf-8
from qgis.core import QgsStyle
from qgis.gui import QgsCategorizedSymbolRendererWidget
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
categorized_symbol_renderer_v2_widget = QgsCategorizedSymbolRendererWidget(
    iface.activeLayer(),
    QgsStyleV2.defaultStyle(),
    iface.activeLayer().rendererV2()
)

# TODO: inspect why qgis crashes
# categorized_symbol_renderer_v2_widget.setMapCanvas(canvas)
# QgsCategorizedSymbolRendererWidget(*args) does not have 
# '.setMapCanvas(canvas)' in api V3
 
def on_widget_changed():
    layer.setRenderer(
        categorized_symbol_renderer_v2_widget.renderer()
    )
    if canvas.isCachingEnabled():
        # layer.setCacheImage(None)
        # QgsVectorLayer does'nt have above attribute in v3
        layer.triggerRepaint()
    else:
        canvas.refresh()

categorized_symbol_renderer_v2_widget.widgetChanged.connect(on_widget_changed)  # Not working with 2.14 version. Need master
categorized_symbol_renderer_v2_widget.show()
