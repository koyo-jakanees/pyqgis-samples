# coding: utf-8
from qgis.core import QgsApplication, QgsCustomColorScheme
from qgis.gui import QgsColorSchemeList, QgsColorSchemeModel

color_scheme_registry = QgsApplication.colorSchemeRegistry()
# """QgsColorSchemeRegistry""":
# This class is no longer a singleton and instance() has been removed.
# Instead use QgsApplication::colorSchemeRegistry() 
# to access an application-wide registry.
# Ref: https://qgis.org/api/api_break.html
# qgis_api_break_3_0_QgsColorSchemeRegistry
schemes = color_scheme_registry.schemes()
project_scheme = [s for s in schemes if isinstance(s, QgsCustomColorScheme)][0]

color_scheme_list = QgsColorSchemeList()
# Doing
color_scheme_model = QgsColorSchemeModel(project_scheme)
color_scheme_list.setModel(color_scheme_model)
# or below do the same: change color in the component
# First option is lower level when you need to reuse
# the model in another component
color_scheme_list.setScheme(project_scheme)

color_scheme_list.show()
