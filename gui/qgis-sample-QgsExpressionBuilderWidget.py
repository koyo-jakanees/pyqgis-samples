# coding: utf-8
from qgis.PyQt.QtWidgets import QWidget
from qgis.gui import QgsExpressionBuilderWidget

w = QWidget()
expression_builder_widget = QgsExpressionBuilderWidget(w)

w.show()
