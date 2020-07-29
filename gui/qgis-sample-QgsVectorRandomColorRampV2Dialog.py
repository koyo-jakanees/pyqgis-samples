# coding: utf-8
from qgis.core import QgsLimitedRandomColorRamp
from qgis.gui import QgsLimitedRandomColorRampDialog

# changed from QgsVectorRandomV2ColorRsmp to QgsLimitedRandomColorRamp
vector_random_color_ramp_v2_dialog = QgsLimitedRandomColorRampDialog(
    QgsLimitedRandomColorRamp()
)

vector_random_color_ramp_v2_dialog.show()
