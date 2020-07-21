# coding: utf-8
from __future__ import print_function
from qgis.PyQt.QtCore import Qt  # http://doc.qt.io/qt-4.8/qwidget.html#windowFlags-prop
from qgis.PyQt.QtGui import QColor  # http://doc.qt.io/qt-4.8/qcolor.html
from qgis.gui import QgsColorDialog 
from qgis.utils import iface

color_dialog_v2 = QgsColorDialog(
    iface.mainWindow(),
    fl=Qt.WindowFlags(),
    color=QColor(0, 255, 127, 127)
)


def on_qcolor_changed(qcolor):
    print(qcolor.name())

color_dialog_v2.currentColorChanged.connect(on_qcolor_changed)

# new_dialog.show()
color_dialog_v2.show()

# Change default value to True to False
color_dialog_v2.setAllowOpacity(False)
