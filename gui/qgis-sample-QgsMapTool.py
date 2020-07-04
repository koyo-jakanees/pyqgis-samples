# coding: utf-8
from __future__ import print_function
from qgis.PyQt.QtCore import Qt
from qgis.gui import QgsMapTool
from qgis.utils import iface


class SendPointToolCoordinates(QgsMapTool):
    """ Enable to return coordinates from clic in a layer.
    """
    def __init__(self, canvas, layer):
        """ Constructor.
        """
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        self.layer = layer
        self.setCursor(Qt.CrossCursor)

    def canvasReleaseEvent(self, event):
        point = self.toLayerCoordinates(self.layer, event.pos())

        # fix_print_with_import
        print((point.x(), point.y()))

layer, canvas = iface.activeLayer(), iface.mapCanvas()

send_point_tool_coordinates = SendPointToolCoordinates(
    canvas,
    layer
)
canvas.setMapTool(send_point_tool_coordinates)
