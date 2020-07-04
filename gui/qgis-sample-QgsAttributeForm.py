# coding: utf-8
from qgis.gui import QgsAttributeForm
from qgis.utils import iface

layer = iface.activeLayer()
attribute_form = QgsAttributeForm(layer, next(layer.getFeatures()))
attribute_form.setMode(mode=0)  # SingleEditMode:0, AddFeatureMode:1, MultiEditMode:2, SearchMode:3

attribute_form.show()
