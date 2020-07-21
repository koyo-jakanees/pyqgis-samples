# coding: utf-8
from qgis.core import QgsCptCityColorRamp
from qgis.gui import QgsCptCityColorRampDialog

cpt_city_color_ramp_v2_dialog = QgsCptCityColorRampDialog(
    QgsCptCityColorRamp()
)

cpt_city_color_ramp_v2_dialog.show()
