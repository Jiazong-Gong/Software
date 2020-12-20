# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '员工登录.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_staffLogin(object):
    def setupUi(self, staffLogin):
        staffLogin.setObjectName("staffLogin")
        staffLogin.resize(491, 407)
        self.centralwidget = QtWidgets.QWidget(staffLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.uiNameForLog = QtWidgets.QLabel(self.centralwidget)
        self.uiNameForLog.setGeometry(QtCore.QRect(150, 80, 201, 51))
        self.uiNameForLog.setObjectName("uiNameForLog")
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setEnabled(True)
        self.lineEditPassword.setGeometry(QtCore.QRect(260, 200, 113, 21))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setEnabled(True)
        self.labelPassword.setGeometry(QtCore.QRect(100, 205, 72, 15))
        self.labelPassword.setObjectName("labelPassword")
        self.labelStaff = QtWidgets.QLabel(self.centralwidget)
        self.labelStaff.setEnabled(True)
        self.labelStaff.setGeometry(QtCore.QRect(100, 155, 72, 15))
        self.labelStaff.setObjectName("labelStaff")
        self.pushButtonClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonClear.setGeometry(QtCore.QRect(300, 270, 40, 40))
        self.pushButtonClear.setText("")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.lineEditStaff = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditStaff.setEnabled(True)
        self.lineEditStaff.setGeometry(QtCore.QRect(260, 150, 113, 21))
        self.lineEditStaff.setObjectName("lineEditStaff")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 330, 72, 15))
        self.label.setStyleSheet("font: 10pt \"新宋体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 330, 72, 15))
        self.label_2.setStyleSheet("font: 10pt \"新宋体\";")
        self.label_2.setObjectName("label_2")
        self.pushButtonOK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOK.setGeometry(QtCore.QRect(120, 270, 40, 40))
        self.pushButtonOK.setText("")
        self.pushButtonOK.setObjectName("pushButtonOK")
        staffLogin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(staffLogin)
        self.statusbar.setObjectName("statusbar")
        staffLogin.setStatusBar(self.statusbar)

        self.retranslateUi(staffLogin)
        QtCore.QMetaObject.connectSlotsByName(staffLogin)

    def retranslateUi(self, staffLogin):
        _translate = QtCore.QCoreApplication.translate
        staffLogin.setWindowTitle(_translate("staffLogin", "登录界面"))
        self.uiNameForLog.setText(_translate("staffLogin", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">员工登陆</span></p></body></html>"))
        self.labelPassword.setText(_translate("staffLogin", "密码"))
        self.labelStaff.setText(_translate("staffLogin", "员工号"))
        self.label.setText(_translate("staffLogin", "确定"))
        self.label_2.setText(_translate("staffLogin", "重新输入"))

