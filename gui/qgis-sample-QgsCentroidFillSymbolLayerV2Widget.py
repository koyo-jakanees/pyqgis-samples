# coding: utf-8
from qgis.gui import QgsCentroidFillSymbolLayerWidget
from qgis.utils import iface

layer = iface.activeLayer()
centroid_fill_symbol_layer_v2_widget = QgsCentroidFillSymbolLayerWidget(
    layer
)

centroid_fill_symbol_layer_v2_widget.show()
