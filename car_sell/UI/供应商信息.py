# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '供应商信息.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowSupply(object):
    def setupUi(self, MainWindowSupply):
        MainWindowSupply.setObjectName("MainWindowSupply")
        MainWindowSupply.resize(762, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindowSupply)
        self.centralwidget.setObjectName("centralwidget")
        self.labelSupplyNo = QtWidgets.QLabel(self.centralwidget)
        self.labelSupplyNo.setGeometry(QtCore.QRect(140, 80, 161, 71))
        self.labelSupplyNo.setStyleSheet("font: 18pt \"新宋体\";")
        self.labelSupplyNo.setObjectName("labelSupplyNo")
        self.lineEditSupplyNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSupplyNo.setGeometry(QtCore.QRect(310, 70, 113, 21))
        self.lineEditSupplyNo.setObjectName("lineEditSupplyNo")
        self.pushButtonSupplySearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSupplySearch.setGeometry(QtCore.QRect(520, 60, 40, 40))
        self.pushButtonSupplySearch.setText("")
        self.pushButtonSupplySearch.setObjectName("pushButtonSupplySearch")
        self.tableWidgetSupplyInfo = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetSupplyInfo.setGeometry(QtCore.QRect(170, 220, 401, 71))
        self.tableWidgetSupplyInfo.setObjectName("tableWidgetSupplyInfo")
        self.tableWidgetSupplyInfo.setColumnCount(3)
        self.tableWidgetSupplyInfo.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSupplyInfo.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSupplyInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSupplyInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSupplyInfo.setHorizontalHeaderItem(2, item)
        self.lineEditDelete = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDelete.setGeometry(QtCore.QRect(310, 150, 113, 21))
        self.lineEditDelete.setObjectName("lineEditDelete")
        self.pushButtonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDelete.setGeometry(QtCore.QRect(520, 140, 40, 40))
        self.pushButtonDelete.setText("")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 110, 72, 15))
        self.label.setStyleSheet("font: 10pt \"新宋体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 200, 72, 15))
        self.label_2.setStyleSheet("font: 10pt \"新宋体\";")
        self.label_2.setObjectName("label_2")
        MainWindowSupply.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowSupply)
        self.statusbar.setObjectName("statusbar")
        MainWindowSupply.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowSupply)
        QtCore.QMetaObject.connectSlotsByName(MainWindowSupply)

    def retranslateUi(self, MainWindowSupply):
        _translate = QtCore.QCoreApplication.translate
        MainWindowSupply.setWindowTitle(_translate("MainWindowSupply", "供应商信息"))
        self.labelSupplyNo.setText(_translate("MainWindowSupply", "供应商\n"
"编号"))
        item = self.tableWidgetSupplyInfo.verticalHeaderItem(0)
        item.setText(_translate("MainWindowSupply", "1"))
        item = self.tableWidgetSupplyInfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowSupply", "编号"))
        item = self.tableWidgetSupplyInfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowSupply", "名称"))
        item = self.tableWidgetSupplyInfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowSupply", "电话"))
        self.label.setText(_translate("MainWindowSupply", "查询"))
        self.label_2.setText(_translate("MainWindowSupply", "删除"))

