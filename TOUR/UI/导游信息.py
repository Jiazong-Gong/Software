# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '导游信息.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowGuide(object):
    def setupUi(self, MainWindowGuide):
        MainWindowGuide.setObjectName("MainWindowGuide")
        MainWindowGuide.resize(735, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindowGuide)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(500, 60, 40, 40))
        self.pushButtonSearch.setText("")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 230, 531, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(290, 80, 113, 21))
        self.lineEditName.setObjectName("lineEditName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 72, 15))
        self.label.setObjectName("label")
        self.pushButtonRegister = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRegister.setGeometry(QtCore.QRect(140, 490, 40, 40))
        self.pushButtonRegister.setText("")
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 120, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 550, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 210, 72, 15))
        self.label_4.setObjectName("label_4")
        self.pushButtonSearchDelete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchDelete.setGeometry(QtCore.QRect(500, 150, 40, 40))
        self.pushButtonSearchDelete.setText("")
        self.pushButtonSearchDelete.setObjectName("pushButtonSearchDelete")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 170, 72, 15))
        self.label_5.setObjectName("label_5")
        self.lineEditNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNo.setGeometry(QtCore.QRect(290, 170, 113, 21))
        self.lineEditNo.setObjectName("lineEditNo")
        MainWindowGuide.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowGuide)
        self.statusbar.setObjectName("statusbar")
        MainWindowGuide.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowGuide)
        QtCore.QMetaObject.connectSlotsByName(MainWindowGuide)

    def retranslateUi(self, MainWindowGuide):
        _translate = QtCore.QCoreApplication.translate
        MainWindowGuide.setWindowTitle(_translate("MainWindowGuide", "导游信息"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindowGuide", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindowGuide", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindowGuide", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindowGuide", "4"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowGuide", "编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowGuide", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowGuide", "电话"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowGuide", "性别"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindowGuide", "年龄"))
        self.label.setText(_translate("MainWindowGuide", "导游姓名"))
        self.label_2.setText(_translate("MainWindowGuide", "查询"))
        self.label_3.setText(_translate("MainWindowGuide", "登记"))
        self.label_4.setText(_translate("MainWindowGuide", "删除"))
        self.label_5.setText(_translate("MainWindowGuide", "导游编号"))

