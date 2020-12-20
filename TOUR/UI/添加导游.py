# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '添加导游.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditGuiudeName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditGuiudeName.setGeometry(QtCore.QRect(340, 110, 113, 21))
        self.lineEditGuiudeName.setObjectName("lineEditGuiudeName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 110, 72, 15))
        self.label.setObjectName("label")
        self.lineEditTele = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTele.setGeometry(QtCore.QRect(340, 180, 113, 21))
        self.lineEditTele.setObjectName("lineEditTele")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 180, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEditGender = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditGender.setGeometry(QtCore.QRect(340, 250, 113, 21))
        self.lineEditGender.setObjectName("lineEditGender")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 250, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEditAge = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAge.setGeometry(QtCore.QRect(340, 320, 113, 21))
        self.lineEditAge.setObjectName("lineEditAge")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 320, 72, 15))
        self.label_4.setObjectName("label_4")
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(270, 430, 40, 40))
        self.pushButtonAdd.setText("")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 490, 72, 15))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "添加导游"))
        self.label.setText(_translate("MainWindow", "导游姓名"))
        self.label_2.setText(_translate("MainWindow", "电话"))
        self.label_3.setText(_translate("MainWindow", "性别"))
        self.label_4.setText(_translate("MainWindow", "年龄"))
        self.label_5.setText(_translate("MainWindow", "添加"))

