# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '景点.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowSights(object):
    def setupUi(self, MainWindowSights):
        MainWindowSights.setObjectName("MainWindowSights")
        MainWindowSights.resize(781, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindowSights)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidgetResults = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetResults.setGeometry(QtCore.QRect(130, 200, 521, 171))
        self.tableWidgetResults.setObjectName("tableWidgetResults")
        self.tableWidgetResults.setColumnCount(4)
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
        self.labelSight = QtWidgets.QLabel(self.centralwidget)
        self.labelSight.setGeometry(QtCore.QRect(150, 90, 72, 15))
        self.labelSight.setObjectName("labelSight")
        self.lineEditSight = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSight.setGeometry(QtCore.QRect(340, 90, 113, 21))
        self.lineEditSight.setObjectName("lineEditSight")
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(550, 70, 40, 40))
        self.pushButtonSearch.setText("")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 130, 72, 15))
        self.label_2.setObjectName("label_2")
        MainWindowSights.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowSights)
        self.statusbar.setObjectName("statusbar")
        MainWindowSights.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowSights)
        QtCore.QMetaObject.connectSlotsByName(MainWindowSights)

    def retranslateUi(self, MainWindowSights):
        _translate = QtCore.QCoreApplication.translate
        MainWindowSights.setWindowTitle(_translate("MainWindowSights", "MainWindow"))
        item = self.tableWidgetResults.verticalHeaderItem(0)
        item.setText(_translate("MainWindowSights", "1"))
        item = self.tableWidgetResults.verticalHeaderItem(1)
        item.setText(_translate("MainWindowSights", "2"))
        item = self.tableWidgetResults.verticalHeaderItem(2)
        item.setText(_translate("MainWindowSights", "3"))
        item = self.tableWidgetResults.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowSights", "编号"))
        item = self.tableWidgetResults.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowSights", "名称"))
        item = self.tableWidgetResults.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowSights", "电话"))
        item = self.tableWidgetResults.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowSights", "价格"))
        self.labelSight.setText(_translate("MainWindowSights", "景点名称"))
        self.label_2.setText(_translate("MainWindowSights", "查询"))

