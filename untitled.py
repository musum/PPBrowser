# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(906, 445)
        self.dockWidget = QtWidgets.QDockWidget(Form)
        self.dockWidget.setGeometry(QtCore.QRect(10, 0, 641, 301))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 271))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.dockWidget_2 = QtWidgets.QDockWidget(Form)
        self.dockWidget_2.setGeometry(QtCore.QRect(660, 0, 221, 301))
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.dockWidgetContents_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 221, 271))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        self.dockWidget_3 = QtWidgets.QDockWidget(Form)
        self.dockWidget_3.setGeometry(QtCore.QRect(10, 300, 641, 121))
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.dockWidgetContents_3)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 641, 91))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        self.dockWidget_4 = QtWidgets.QDockWidget(Form)
        self.dockWidget_4.setGeometry(QtCore.QRect(660, 300, 231, 121))
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.dockWidgetContents_4)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 231, 91))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_4.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_4.addTab(self.tab_8, "")
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("Form", "Tab 1"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("Form", "Tab 2"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Form", "Tab 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "Tab 2"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), _translate("Form", "Tab 1"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_8), _translate("Form", "Tab 2"))

