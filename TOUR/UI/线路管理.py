# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '线路管理.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowRoute(object):
    def setupUi(self, MainWindowRoute):
        MainWindowRoute.setObjectName("MainWindowRoute")
        MainWindowRoute.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindowRoute)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 40, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 40, 72, 15))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 30, 40, 40))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 130, 281, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 40, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 90, 72, 15))
        self.label.setObjectName("label")
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(130, 460, 93, 28))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        MainWindowRoute.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowRoute)
        self.statusbar.setObjectName("statusbar")
        MainWindowRoute.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowRoute)
        QtCore.QMetaObject.connectSlotsByName(MainWindowRoute)

    def retranslateUi(self, MainWindowRoute):
        _translate = QtCore.QCoreApplication.translate
        MainWindowRoute.setWindowTitle(_translate("MainWindowRoute", "线路查询"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindowRoute", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindowRoute", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindowRoute", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindowRoute", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindowRoute", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindowRoute", "6"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowRoute", "线路编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowRoute", "景点名称"))
        self.label_4.setText(_translate("MainWindowRoute", "线路编号"))
        self.label.setText(_translate("MainWindowRoute", "查询"))
        self.pushButtonAdd.setText(_translate("MainWindowRoute", "添加线路"))

