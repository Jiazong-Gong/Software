# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '库存查询.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CarLib(object):
    def setupUi(self, CarLib):
        CarLib.setObjectName("CarLib")
        CarLib.resize(800, 627)
        self.centralwidget = QtWidgets.QWidget(CarLib)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidgetLib = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetLib.setGeometry(QtCore.QRect(130, 190, 521, 291))
        self.tableWidgetLib.setObjectName("tableWidgetLib")
        self.tableWidgetLib.setColumnCount(4)
        self.tableWidgetLib.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLib.setHorizontalHeaderItem(3, item)
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(560, 30, 40, 40))
        self.pushButtonSearch.setText("")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.lineEditBrandSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditBrandSearch.setGeometry(QtCore.QRect(330, 50, 113, 21))
        self.lineEditBrandSearch.setObjectName("lineEditBrandSearch")
        self.labelBrandSearch = QtWidgets.QLabel(self.centralwidget)
        self.labelBrandSearch.setGeometry(QtCore.QRect(160, 50, 71, 21))
        self.labelBrandSearch.setStyleSheet("font: 10pt \"新宋体\";")
        self.labelBrandSearch.setObjectName("labelBrandSearch")
        self.pushButtonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDelete.setGeometry(QtCore.QRect(560, 110, 40, 40))
        self.pushButtonDelete.setText("")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.lineEditDelete = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDelete.setGeometry(QtCore.QRect(330, 110, 113, 21))
        self.lineEditDelete.setObjectName("lineEditDelete")
        self.labelNameDelete = QtWidgets.QLabel(self.centralwidget)
        self.labelNameDelete.setGeometry(QtCore.QRect(160, 110, 71, 21))
        self.labelNameDelete.setStyleSheet("font: 10pt \"新宋体\";")
        self.labelNameDelete.setObjectName("labelNameDelete")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 80, 72, 15))
        self.label.setStyleSheet("font: 10pt \"新宋体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 160, 72, 15))
        self.label_2.setStyleSheet("font: 10pt \"新宋体\";")
        self.label_2.setObjectName("label_2")
        CarLib.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CarLib)
        self.statusbar.setObjectName("statusbar")
        CarLib.setStatusBar(self.statusbar)

        self.retranslateUi(CarLib)
        QtCore.QMetaObject.connectSlotsByName(CarLib)

    def retranslateUi(self, CarLib):
        _translate = QtCore.QCoreApplication.translate
        CarLib.setWindowTitle(_translate("CarLib", "库存查询"))
        item = self.tableWidgetLib.verticalHeaderItem(0)
        item.setText(_translate("CarLib", "1"))
        item = self.tableWidgetLib.verticalHeaderItem(1)
        item.setText(_translate("CarLib", "2"))
        item = self.tableWidgetLib.verticalHeaderItem(2)
        item.setText(_translate("CarLib", "3"))
        item = self.tableWidgetLib.verticalHeaderItem(3)
        item.setText(_translate("CarLib", "4"))
        item = self.tableWidgetLib.verticalHeaderItem(4)
        item.setText(_translate("CarLib", "5"))
        item = self.tableWidgetLib.verticalHeaderItem(5)
        item.setText(_translate("CarLib", "6"))
        item = self.tableWidgetLib.verticalHeaderItem(6)
        item.setText(_translate("CarLib", "7"))
        item = self.tableWidgetLib.horizontalHeaderItem(0)
        item.setText(_translate("CarLib", "编号"))
        item = self.tableWidgetLib.horizontalHeaderItem(1)
        item.setText(_translate("CarLib", "名称"))
        item = self.tableWidgetLib.horizontalHeaderItem(2)
        item.setText(_translate("CarLib", "单价"))
        item = self.tableWidgetLib.horizontalHeaderItem(3)
        item.setText(_translate("CarLib", "数量"))
        self.labelBrandSearch.setText(_translate("CarLib", "汽车品牌"))
        self.labelNameDelete.setText(_translate("CarLib", "汽车名称"))
        self.label.setText(_translate("CarLib", "查询"))
        self.label_2.setText(_translate("CarLib", "删除"))

