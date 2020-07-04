# coding: utf-8
from qgis.PyQt.QtCore import QUrl
from qgis.PyQt.QtNetwork import QNetworkRequest
from qgis.core import QgsNetworkAccessManager
from qgis.gui import QgsAuthSslErrorsDialog

url = 'http://fm4dd.com/openssl/source/PEM/certs/1024b-rsa-example-cert.pem'

networkAccessManager = QgsNetworkAccessManager.instance()
req = QNetworkRequest(QUrl(url))
reply = networkAccessManager.get(req)  # Return a QNetworkReply (http://doc.qt.io/qt-4.8/qnetworkreply.html)

auth_ssl_errors_dialog = QgsAuthSslErrorsDialog(
    reply, [
        QSslError(QSslError.InvalidNotAfterField)
    ]
)

auth_ssl_errors_dialog.show()
