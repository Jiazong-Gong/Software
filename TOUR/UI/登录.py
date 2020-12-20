# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '登录.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowLogin(object):
    def setupUi(self, MainWindowLogin):
        MainWindowLogin.setObjectName("MainWindowLogin")
        MainWindowLogin.resize(492, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindowLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.uiNameForLog = QtWidgets.QLabel(self.centralwidget)
        self.uiNameForLog.setGeometry(QtCore.QRect(160, 70, 201, 51))
        self.uiNameForLog.setObjectName("uiNameForLog")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 320, 72, 15))
        self.label_2.setStyleSheet("font: 10pt \"新宋体\";")
        self.label_2.setObjectName("label_2")
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setEnabled(True)
        self.lineEditPassword.setGeometry(QtCore.QRect(270, 190, 113, 21))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonOK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOK.setGeometry(QtCore.QRect(130, 260, 40, 40))
        self.pushButtonOK.setText("")
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.lineEditStaff = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditStaff.setEnabled(True)
        self.lineEditStaff.setGeometry(QtCore.QRect(270, 140, 113, 21))
        self.lineEditStaff.setObjectName("lineEditStaff")
        self.labelStaff = QtWidgets.QLabel(self.centralwidget)
        self.labelStaff.setEnabled(True)
        self.labelStaff.setGeometry(QtCore.QRect(110, 145, 72, 15))
        self.labelStaff.setObjectName("labelStaff")
        self.pushButtonClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonClear.setGeometry(QtCore.QRect(310, 260, 40, 40))
        self.pushButtonClear.setText("")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setEnabled(True)
        self.labelPassword.setGeometry(QtCore.QRect(110, 195, 72, 15))
        self.labelPassword.setObjectName("labelPassword")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 320, 72, 15))
        self.label.setStyleSheet("font: 10pt \"新宋体\";")
        self.label.setObjectName("label")
        MainWindowLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindowLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowLogin)
        self.statusbar.setObjectName("statusbar")
        MainWindowLogin.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindowLogin)
        QtCore.QMetaObject.connectSlotsByName(MainWindowLogin)

    def retranslateUi(self, MainWindowLogin):
        _translate = QtCore.QCoreApplication.translate
        MainWindowLogin.setWindowTitle(_translate("MainWindowLogin", "MainWindow"))
        self.uiNameForLog.setText(_translate("MainWindowLogin", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">员工登陆</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindowLogin", "重新输入"))
        self.labelStaff.setText(_translate("MainWindowLogin", "员工号"))
        self.labelPassword.setText(_translate("MainWindowLogin", "密码"))
        self.label.setText(_translate("MainWindowLogin", "确定"))
        self.menu.setTitle(_translate("MainWindowLogin", "登陆界面"))

