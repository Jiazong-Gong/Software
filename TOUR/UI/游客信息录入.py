# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '游客信息录入.ui'
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 80, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 150, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 220, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 290, 72, 15))
        self.label_4.setObjectName("label_4")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(390, 80, 113, 21))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditTele = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTele.setGeometry(QtCore.QRect(390, 150, 113, 21))
        self.lineEditTele.setObjectName("lineEditTele")
        self.lineEditAge = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAge.setGeometry(QtCore.QRect(390, 220, 113, 21))
        self.lineEditAge.setObjectName("lineEditAge")
        self.lineEditGender = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditGender.setGeometry(QtCore.QRect(390, 290, 113, 21))
        self.lineEditGender.setObjectName("lineEditGender")
        self.lineEditTourGroup = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTourGroup.setGeometry(QtCore.QRect(390, 360, 113, 21))
        self.lineEditTourGroup.setObjectName("lineEditTourGroup")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 360, 91, 16))
        self.label_5.setObjectName("label_5")
        self.pushButtonOK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOK.setGeometry(QtCore.QRect(300, 440, 40, 40))
        self.pushButtonOK.setText("")
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 500, 72, 15))
        self.label_6.setObjectName("label_6")
        MainWindowTourists.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowTourists)
        self.statusbar.setObjectName("statusbar")
        MainWindowTourists.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowTourists)
        QtCore.QMetaObject.connectSlotsByName(MainWindowTourists)

    def retranslateUi(self, MainWindowTourists):
        _translate = QtCore.QCoreApplication.translate
        MainWindowTourists.setWindowTitle(_translate("MainWindowTourists", "游客登记"))
        self.label.setText(_translate("MainWindowTourists", "姓名"))
        self.label_2.setText(_translate("MainWindowTourists", "电话"))
        self.label_3.setText(_translate("MainWindowTourists", "年龄"))
        self.label_4.setText(_translate("MainWindowTourists", "性别"))
        self.label_5.setText(_translate("MainWindowTourists", "旅行团编号"))
        self.label_6.setText(_translate("MainWindowTourists", "录入"))

