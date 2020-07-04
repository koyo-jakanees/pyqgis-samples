# coding: utf-8
from qgis.PyQt.QtCore import Qt
from qgis.gui import QgsBusyIndicatorDialog
from qgis.utils import iface

main_window = iface.mainWindow()
busy_indicator_dialog = QgsBusyIndicatorDialog("Waiting", main_window,
                                               fl=Qt.WindowFlags())

busy_indicator_dialog.show()
