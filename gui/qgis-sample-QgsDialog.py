# coding: utf-8
from qgis.PyQt.QtCore import Qt  # http://doc.qt.io/qt-4.8/qwidget.html#windowFlags-prop
from qgis.PyQt.QtWidgets import QDialogButtonBox  # http://doc.qt.io/qt-4.8/qcolor.html
from qgis.gui import QgsDialog
from qgis.utils import iface

main_window = iface.mainWindow()
dialog = QgsDialog(main_window,
                   fl=Qt.WindowFlags(),
                   buttons=QDialogButtonBox.Close,
                   orientation=Qt.Horizontal)
dialog.resize(600, 400)

dialog.show()
