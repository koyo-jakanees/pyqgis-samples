# coding: utf-8
from qgis.gui import QgsAttributeForm
from qgis.utils import iface

layer = iface.activeLayer()
context = ""
f = QgsFeature()
attribute_form = QgsAttributeForm(layer, layer.getFeatures().__next__())
# rename 'next' to '__next__()'
attribute_form.Mode(QgsAttributeForm.AddFeatureMode)  # SingleEditMode, AddFeatureMode, MultiEditMode, SearchMode
# change from "attribute_fomrm.setMode" to "attribute_form.Mode"
attribute_form.show()