# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '顾客信息登记.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowCustmerInfoRegister(object):
    def setupUi(self, MainWindowCustmerInfoRegister):
        MainWindowCustmerInfoRegister.setObjectName("MainWindowCustmerInfoRegister")
        MainWindowCustmerInfoRegister.resize(752, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindowCustmerInfoRegister)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditCustmerName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCustmerName.setEnabled(True)
        self.lineEditCustmerName.setGeometry(QtCore.QRect(400, 180, 113, 21))
        self.lineEditCustmerName.setObjectName("lineEditCustmerName")
        self.lineEditCustmerID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCustmerID.setEnabled(True)
        self.lineEditCustmerID.setGeometry(QtCore.QRect(400, 280, 113, 21))
        self.lineEditCustmerID.setObjectName("lineEditCustmerID")
        self.labelCustmerName = QtWidgets.QLabel(self.centralwidget)
        self.labelCustmerName.setEnabled(True)
        self.labelCustmerName.setGeometry(QtCore.QRect(240, 185, 72, 15))
        self.labelCustmerName.setObjectName("labelCustmerName")
        self.pushButtonReinput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReinput.setGeometry(QtCore.QRect(440, 410, 40, 40))
        self.pushButtonReinput.setText("")
        self.pushButtonReinput.setObjectName("pushButtonReinput")
        self.lineEditCustmerTele = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCustmerTele.setGeometry(QtCore.QRect(400, 330, 113, 21))
        self.lineEditCustmerTele.setObjectName("lineEditCustmerTele")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 110, 281, 51))
        self.label_7.setObjectName("label_7")
        self.labelCustmerTele = QtWidgets.QLabel(self.centralwidget)
        self.labelCustmerTele.setGeometry(QtCore.QRect(240, 335, 72, 15))
        self.labelCustmerTele.setObjectName("labelCustmerTele")
        self.pushButtonOK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOK.setEnabled(True)
        self.pushButtonOK.setGeometry(QtCore.QRect(230, 410, 40, 40))
        self.pushButtonOK.setText("")
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.labelCustmerID = QtWidgets.QLabel(self.centralwidget)
        self.labelCustmerID.setEnabled(True)
        self.labelCustmerID.setGeometry(QtCore.QRect(240, 285, 81, 16))
        self.labelCustmerID.setObjectName("labelCustmerID")
        self.labelCustmerGender = QtWidgets.QLabel(self.centralwidget)
        self.labelCustmerGender.setEnabled(True)
        self.labelCustmerGender.setGeometry(QtCore.QRect(240, 230, 72, 20))
        self.labelCustmerGender.setObjectName("labelCustmerGender")
        self.lineEditCustmerGender = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCustmerGender.setGeometry(QtCore.QRect(400, 230, 113, 21))
        self.lineEditCustmerGender.setObjectName("lineEditCustmerGender")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 470, 72, 15))
        self.label.setStyleSheet("font: 10pt \"新宋体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 470, 72, 15))
        self.label_2.setStyleSheet("font: 10pt \"新宋体\";")
        self.label_2.setObjectName("label_2")
        MainWindowCustmerInfoRegister.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowCustmerInfoRegister)
        self.statusbar.setObjectName("statusbar")
        MainWindowCustmerInfoRegister.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowCustmerInfoRegister)
        QtCore.QMetaObject.connectSlotsByName(MainWindowCustmerInfoRegister)

    def retranslateUi(self, MainWindowCustmerInfoRegister):
        _translate = QtCore.QCoreApplication.translate
        MainWindowCustmerInfoRegister.setWindowTitle(_translate("MainWindowCustmerInfoRegister", "顾客信息登记"))
        self.labelCustmerName.setText(_translate("MainWindowCustmerInfoRegister", "顾客姓名"))
        self.label_7.setText(_translate("MainWindowCustmerInfoRegister", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">顾客信息登记</span></p></body></html>"))
        self.labelCustmerTele.setText(_translate("MainWindowCustmerInfoRegister", "电话号码"))
        self.labelCustmerID.setText(_translate("MainWindowCustmerInfoRegister", "身份证号码"))
        self.labelCustmerGender.setText(_translate("MainWindowCustmerInfoRegister", "性别"))
        self.label.setText(_translate("MainWindowCustmerInfoRegister", "确定"))
        self.label_2.setText(_translate("MainWindowCustmerInfoRegister", "重新输入"))

