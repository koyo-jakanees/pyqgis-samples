# coding: utf-8
from qgis.gui import QgsAttributeForm
from qgis.utils import iface

layer = iface.activeLayer()
attribute_form = QgsAttributeForm(layer, next(layer.getFeatures()))
attribute_form.setMode(QgsAttributeForm.SingleEditMode)  # SingleEditMode, AddFeatureMode, MultiEditMode, SearchMode

attribute_form.show()
