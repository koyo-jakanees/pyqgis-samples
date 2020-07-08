# coding: utf-8
from __future__ import print_function
# from qgis.PyQt .QtWidgets import QWidget
from qgis.gui import QgsActionMenu
from qgis.utils import iface

# qwt = QWidget()
layer = iface.activeLayer()
if iface.activeLayer().actions():
#  AttributeError: 'QgsActionManager' object has no attribute 'size' (Manual refactor!!!)
# actionScope: str = 'Canvas, Field, Feature, Layer' or '' to list all actionScopes
# QgsActionMenu(layer: QgsVectorLayer, feature: QgsFeature, actionScope: str, parent: QWidget = None
# QgsActionMenu(layer: QgsVectorLayer, fid: int, actionScope: str, parent: QWidget = None)
# :param fid: The feature id of the feature for which this action will be run.
    features = layer.dataProvider().getFeatures()
    feat1 = next(features)
    action_menu = QgsActionMenu(
        layer,
        feat1,'Feature'
    )
    print(feat1.id())

    action_menu.show()
    print(action_menu.actions())
    feat2 = next(features)
    action_menu.setFeature(feat2)
    print(feat2.id())
else:
    print('No action for this layer')

