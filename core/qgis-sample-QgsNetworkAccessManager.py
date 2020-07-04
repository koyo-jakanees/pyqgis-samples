# coding:utf-8
from __future__ import print_function
from qgis.PyQt.QtCore import QUrl
from qgis.PyQt.QtNetwork import QNetworkRequest
from qgis.core import QgsNetworkAccessManager

url = 'http://qgis.org/en/site/'


def urlCallFinished(reply):
    print(reply.readAll())
    reply.deleteLater()

networkAccessManager = QgsNetworkAccessManager.instance()
# Will work when running from a single file or it will not work
networkAccessManager.finished.connect(urlCallFinished)

req = QNetworkRequest(QUrl(url))
reply = networkAccessManager.get(req)  # Return a QNetworkReply (http://doc.qt.io/qt-4.8/qnetworkreply.html)
