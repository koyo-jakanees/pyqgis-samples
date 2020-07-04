# coding: utf-8
from __future__ import print_function
from qgis.PyQt.QtWidgets import QDialog
from qgis.gui import QgsAuthCertTrustPolicyComboBox

new_dialog = QDialog()
new_dialog.resize(800, 600)

auth_cert_trust_policy_combo_box = QgsAuthCertTrustPolicyComboBox(new_dialog)


def on_cert_changed(s):
    print(auth_cert_trust_policy_combo_box.trustPolicy())
    print("Auth cert changed")

auth_cert_trust_policy_combo_box.currentIndexChanged.connect(on_cert_changed)

new_dialog.show()
