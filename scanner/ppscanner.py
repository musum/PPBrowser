import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from scanner.mainwindow import Ui_MainWindow
from scanner.dialog import Ui_Dialog


class DlgAdd(QDialog, Ui_Dialog):
    def __init__(self, title, parent=None):
        super(DlgAdd, self).__init__(parent)
        self.title = title
        self.setupUi(self)
        self.setWindowTitle(title)
        self.lineEdit.returnPressed.connect(self.on_add)
        self.pushButton.clicked.connect(self.on_add)
        self.lineEdit.setFocus()

        self.items = []

    def on_add(self):
        text = self.lineEdit.text()
        data = text.split(',')
        self.items += data
        self.parent().__getattr__('listWidget_%ss' % self.title).additems(data)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionAbout.triggered.connect(self.on_about)
        self.actionExit.triggered.connect(self.on_exit)
        self.pushButton_addip.clicked.connect(self.on_addip)
        self.pushButton_addport.clicked.connect(self.on_addport)
        self.pushButton_cleanip.clicked.connect(self.on_cleanip)
        self.pushButton_cleanport.clicked.connect(self.on_cleanport)
        self.pushButton_delip.clicked.connect(self.on_delip)
        self.pushButton_delport.clicked.connect(self.on_delport)
        self.pushButton_scan.clicked.connect(self.on_scan)

        self.iplist = []
        self.portlist = []
        self.listWidget_ports

    def on_about(self):
        print('About')

    def on_exit(self):
        btn = QMessageBox.question(self, "退出", "是否确定退出？",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if btn == QMessageBox.Ok:
            qApp.quit()

    def on_addip(self):
        dlg = DlgAdd('ip', self)
        pass

    def on_addport(self):
        pass

    def on_cleanip(self):
        pass

    def on_cleanport(self):
        pass

    def on_delip(self):
        pass

    def on_delport(self):
        pass

    def on_scan(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

