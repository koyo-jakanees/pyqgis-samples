# coding: utf-8
from qgis.core import QgsGradientColorRamp
from qgis.gui import QgsGradientColorRampDialog

gradient_color_ramp_dialog = QgsGradientColorRampDialog(
    QgsGradientColorRamp()
)
gradient_color_ramp_dialog.show()
