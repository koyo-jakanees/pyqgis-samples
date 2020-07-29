# coding: utf-8
from qgis.core import QgsColorBrewerColorRamp
from qgis.gui import QgsColorBrewerColorRampDialog

color_brewer_color_ramp_dialog = QgsColorBrewerColorRampDialog(
    QgsColorBrewerColorRamp()
)

color_brewer_color_ramp_dialog.show()
