# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '添加酒店.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(320, 440, 40, 40))
        self.pushButtonAdd.setText("")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 60, 72, 15))
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEditCity = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCity.setGeometry(QtCore.QRect(400, 140, 113, 21))
        self.lineEditCity.setObjectName("lineEditCity")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 140, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEditTele = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTele.setGeometry(QtCore.QRect(400, 200, 113, 21))
        self.lineEditTele.setObjectName("lineEditTele")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 200, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEditType = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditType.setGeometry(QtCore.QRect(400, 260, 113, 21))
        self.lineEditType.setObjectName("lineEditType")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 260, 72, 15))
        self.label_4.setObjectName("label_4")
        self.lineEditMax = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMax.setGeometry(QtCore.QRect(400, 320, 113, 21))
        self.lineEditMax.setObjectName("lineEditMax")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 320, 72, 15))
        self.label_5.setObjectName("label_5")
        self.lineEditPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPrice.setGeometry(QtCore.QRect(400, 380, 113, 21))
        self.lineEditPrice.setObjectName("lineEditPrice")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 380, 72, 15))
        self.label_6.setObjectName("label_6")
        self.lineEditHotelName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditHotelName.setGeometry(QtCore.QRect(400, 80, 113, 21))
        self.lineEditHotelName.setObjectName("lineEditHotelName")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 80, 72, 15))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 500, 72, 15))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "添加酒店"))
        self.label_2.setText(_translate("MainWindow", "所在城市"))
        self.label_3.setText(_translate("MainWindow", "电话"))
        self.label_4.setText(_translate("MainWindow", "类型"))
        self.label_5.setText(_translate("MainWindow", "容纳人数"))
        self.label_6.setText(_translate("MainWindow", "价格"))
        self.label_7.setText(_translate("MainWindow", "名称"))
        self.label_8.setText(_translate("MainWindow", "添加酒店"))

