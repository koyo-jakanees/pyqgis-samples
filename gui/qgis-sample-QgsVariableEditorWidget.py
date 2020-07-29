# coding: utf-8
from __future__ import print_function
from qgis.core import QgsProject, QgsExpressionContextUtils, QgsExpressionContext
from qgis.gui import QgsVariableEditorWidget
from qgis.utils import iface


project = QgsProject.instance()
canvas = iface.mapCanvas()
variable_editor_widget = QgsVariableEditorWidget()
expression_context = QgsExpressionContext()
expression_context.appendScope(QgsExpressionContextUtils.globalScope())
expression_context.appendScope(QgsExpressionContextUtils.projectScope(project))
# QgsExpressionContextUtils.projectScope(project: QgsProject)-> QgsExpressionContextScope
expression_context.appendScope(QgsExpressionContextUtils.mapSettingsScope(
    canvas.mapSettings()
))
# mapSettingsScope(mapSettings: QgsMapSettings) -> QgsExpressionContextScope
variable_editor_widget.setContext(expression_context)

variable_editor_widget.reloadContext()
variable_editor_widget.setEditableScopeIndex(0)
print(variable_editor_widget.context())
print(variable_editor_widget.editableScope())
print(variable_editor_widget.settingGroup())
print(variable_editor_widget.variablesInActiveScope())

variable_editor_widget.show()
