# coding: utf-8
from qgis.core import QgsCustomColorScheme, QgsApplication
from qgis.gui import QgsColorSchemeList

color_scheme_registry = QgsApplication.colorSchemeRegistry()
# """QgsColorSchemeRegistry""":
# This class is no longer a singleton and instance() has been removed.
# Instead use QgsApplication::colorSchemeRegistry() 
# to access an application-wide registry.
# Ref: https://qgis.org/api/api_break.html#qgis_api_break_3_0_QgsColorSchemeRegistry
schemes = color_scheme_registry.schemes()
project_scheme = [s for s in schemes if isinstance(s, QgsCustomColorScheme)][0]

color_scheme_list = QgsColorSchemeList(scheme=project_scheme)

color_scheme_list.show()

