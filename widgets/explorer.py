import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget, QTreeView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.items = ['呵呵', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff','g', 'h', 'i', 'j', 'k', 'l', 'm'
            ,'m','n','o','p','q','r','s','t']
        self.init()
        self.addDock()


    def init(self):
        self.text = QTextEdit('主窗口')
        self.text.setAlignment(Qt.AlignCenter)
        # self.setCentralWidget(self.text)

        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)

        self.setCentralWidget(self.dataView)

        model = self.create_model(self, ['from', 'sub', 'date'])
        self.dataView.setModel(model)
        self.add_data(model, ['service@github.com', 'Your Github Donation','03/25/2017 02:05 PM'])
        self.setGeometry(200, 200, 800, 400)
        self.setWindowTitle('QDockWidget示例')
        self.show()

    def onDockListIndexChanged(self, index):
        item = self.items[index]
        self.text.setText(item)

    def addDock(self):
        dock1 = QDockWidget('DockWidget')
        dock1.setFeatures(QDockWidget.DockWidgetFloatable)
        dock1.setAllowedAreas(Qt.LeftDockWidgetArea)
        listwidget = QListWidget()

        listwidget.addItems(self.items)
        listwidget.currentRowChanged.connect(self.onDockListIndexChanged)
        dock1.setWidget(listwidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

    def create_model(self, parent, columns=['column1']):
        model = QStandardItemModel(0, len(columns), parent)
        for k, v in enumerate(columns):
            model.setHeaderData(k, Qt.Horizontal, v)
        return model

    def add_data(self, model, data):
        model.insertRow(0)
        for k, v in enumerate(data):
            model.setData(model.index(0, k), v)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


# 入口
if __name__ == '__main__':
    main()