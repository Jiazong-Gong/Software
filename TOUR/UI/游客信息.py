# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '游客信息.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowTourists(object):
    def setupUi(self, MainWindowTourists):
        MainWindowTourists.setObjectName("MainWindowTourists")
        MainWindowTourists.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindowTourists)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(560, 60, 40, 40))
        self.pushButtonSearch.setText("")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.tableWidgetResults = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetResults.setGeometry(QtCore.QRect(50, 170, 701, 171))
        self.tableWidgetResults.setObjectName("tableWidgetResults")
        self.tableWidgetResults.setColumnCount(6)
        self.tableWidgetResults.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setHorizontalHeaderItem(5, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 70, 72, 15))
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(340, 70, 113, 21))
        self.lineEditName.setObjectName("lineEditName")
        self.pushButtonRegister = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRegister.setGeometry(QtCore.QRect(170, 450, 40, 40))
        self.pushButtonRegister.setText("")
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 120, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 510, 72, 15))
        self.label_3.setObjectName("label_3")
        MainWindowTourists.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowTourists)
        self.statusbar.setObjectName("statusbar")
        MainWindowTourists.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowTourists)
        QtCore.QMetaObject.connectSlotsByName(MainWindowTourists)

    def retranslateUi(self, MainWindowTourists):
        _translate = QtCore.QCoreApplication.translate
        MainWindowTourists.setWindowTitle(_translate("MainWindowTourists", "游客信息"))
        item = self.tableWidgetResults.verticalHeaderItem(0)
        item.setText(_translate("MainWindowTourists", "1"))
        item = self.tableWidgetResults.verticalHeaderItem(1)
        item.setText(_translate("MainWindowTourists", "2"))
        item = self.tableWidgetResults.verticalHeaderItem(2)
        item.setText(_translate("MainWindowTourists", "3"))
        item = self.tableWidgetResults.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowTourists", "编号"))
        item = self.tableWidgetResults.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowTourists", "姓名"))
        item = self.tableWidgetResults.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowTourists", "性别"))
        item = self.tableWidgetResults.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowTourists", "电话"))
        item = self.tableWidgetResults.horizontalHeaderItem(4)
        item.setText(_translate("MainWindowTourists", "年龄"))
        item = self.tableWidgetResults.horizontalHeaderItem(5)
        item.setText(_translate("MainWindowTourists", "旅行团编号"))
        self.label.setText(_translate("MainWindowTourists", "游客姓名"))
        self.label_2.setText(_translate("MainWindowTourists", "查询"))
        self.label_3.setText(_translate("MainWindowTourists", "登记"))

