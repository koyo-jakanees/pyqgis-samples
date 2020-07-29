# coding: utf-8
from qgis.PyQt.QtCore import Qt
from qgis.core import QgsCoordinateReferenceSystem
from qgis.gui import QgsUserInputWidget, QgsProjectionSelectionWidget
from qgis.utils import iface

projection_selection_widget = QgsProjectionSelectionWidget()
projection_selection_widget.resize(400, 100)
projection_selection_widget.setCrs(QgsCoordinateReferenceSystem("EPSG:4326"))

# QgsUserInputDockWidget changed to QgsUserInputWidget
# The QgsUserInputWidget class is a floating widget that shall be used to display widgets for user inputs.
# It can be used by map tools, plugins, etc.
user_input_widget = QgsUserInputWidget()


# The widget is automatically hidden if it contains no widget.
user_input_widget.addUserInputWidget(projection_selection_widget)
user_input_widget.setWindowTitle("User Input Dialog")
# user_input_widget.setSizeIncrement(200, 200) # set widget increment to make it visible
# user_input_widget.show()  # -> shows the Dialog as a floatingWdget

iface.addUserInputWidget(user_input_widget)
# user_input_widget.destroy()
# iface.removeDockWidget(user_input_dock_widget)
