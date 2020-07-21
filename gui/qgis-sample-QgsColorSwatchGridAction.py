# coding: utf-8
from qgis.PyQt.QtWidgets import QDialog, QMenu, QMenuBar, QVBoxLayout
from qgis.core import QgsApplication, QgsCustomColorScheme
from qgis.gui import QgsColorSwatchGrid

new_dialog = QDialog()
main_layout = QVBoxLayout()
menu_bar = QMenuBar()
menu = QMenu(u"Test")

color_scheme_registry = QgsApplication.colorSchemeRegistry()
# """QgsColorSchemeRegistry""":
# This class is no longer a singleton and instance() has been removed.
# Instead use QgsApplication::colorSchemeRegistry() 
# to access an application-wide registry.
# Ref: https://qgis.org/api/api_break.html
# qgis_api_break_3_0_QgsColorSchemeRegistry
schemes = color_scheme_registry.schemes()
project_scheme = [s for s in schemes if isinstance(s, QgsCustomColorScheme)][0]

color_swatch_grid_action = QgsColorSwatchGridAction(project_scheme, menu)

menu.addAction(color_swatch_grid_action)

menu_bar.addMenu(menu)
main_layout.setMenuBar(menu_bar)
new_dialog.setLayout(main_layout)

new_dialog.show()
