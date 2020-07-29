# coding:utf-8
from __future__ import print_function
from qgis.PyQt.QtWidgets import QTreeView
from qgis.core import QgsStyle
from qgis.gui import QgsRuleBasedRendererWidget
from qgis.utils import iface

layer = iface.activeLayer()
canvas = iface.mapCanvas()
rule_based_renderer_v2_widget = QgsRuleBasedRendererWidget(
    layer,
    QgsStyle.defaultStyle(),
    layer.renderer()
)

rule_based_renderer_v2_widget.context()
# https://qgis.org/api/api_break.html

def on_widget_changed():
    layer.setRenderer(
        rule_based_renderer_v2_widget.renderer()
    )
    if canvas.isCachingEnabled():
        layer.setCacheImage(None)
        layer.triggerRepaint()
    else:
        canvas.refresh()

rule_based_renderer_v2_widget.widgetChanged.connect(on_widget_changed)
rule_based_renderer_v2_widget.show()

print(
    rule_based_renderer_v2_widget.findChildren(
        QTreeView,
        "viewRules"
    )[0].model()
)  # Issue: it returns a PyQt5.QtCore.QAbstractItemModel whereas it should
# return a QgsRuleBasedRendererV2Model according to code e.g
# https://qgis.org/api/qgsrulebasedrendererv2widget_8cpp_source.html#l00068
