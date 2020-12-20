# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '旅行团信息.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(743, 527)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(490, 70, 40, 40))
        self.pushButtonSearch.setText("")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.tableWidgetResults = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetResults.setGeometry(QtCore.QRect(120, 190, 491, 91))
        self.tableWidgetResults.setObjectName("tableWidgetResults")
        self.tableWidgetResults.setColumnCount(7)
        self.tableWidgetResults.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setVerticalHeaderItem(0, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetResults.setHorizontalHeaderItem(6, item)
        self.lineEditTourGroupNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTourGroupNo.setGeometry(QtCore.QRect(300, 80, 113, 21))
        self.lineEditTourGroupNo.setObjectName("lineEditTourGroupNo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 101, 16))
        self.label.setObjectName("label")
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(190, 380, 40, 40))
        self.pushButtonAdd.setText("")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 140, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 440, 72, 15))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "旅行团信息"))
        item = self.tableWidgetResults.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "编号"))
        item = self.tableWidgetResults.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "酒店"))
        item = self.tableWidgetResults.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "线路编号"))
        item = self.tableWidgetResults.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "导游编号"))
        item = self.tableWidgetResults.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "出行方式编号"))
        item = self.tableWidgetResults.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "价格"))
        item = self.tableWidgetResults.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "出发时间"))
        self.label.setText(_translate("MainWindow", "旅行团编号"))
        self.label_2.setText(_translate("MainWindow", "查询"))
        self.label_3.setText(_translate("MainWindow", "添加"))

