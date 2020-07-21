# coding: utf-8
from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout
from qgis.gui import QgsColorButton

# Create dialog and widget
d = QDialog()
# Create the color button
btn = QgsColorButton()

# Create layout and add the button as a widget to it
vbox = QVBoxLayout()
vbox.addWidget(btn)

# Set the dialog layout
d.setLayout(vbox)

# Show the dialog and hence, the QgsColorButtonV2
d.show()
