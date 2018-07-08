from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

app = QApplication([])
view = QWebEngineView()
view.load(QUrl("http://www.baidu.com"))
view.show()
app.exec_()