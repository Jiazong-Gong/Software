# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '购买.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_carPurchase(object):
    def setupUi(self, carPurchase):
        carPurchase.setObjectName("carPurchase")
        carPurchase.resize(800, 588)
        self.centralwidget = QtWidgets.QWidget(carPurchase)
        self.centralwidget.setObjectName("centralwidget")
        self.labelStaffNo = QtWidgets.QLabel(self.centralwidget)
        self.labelStaffNo.setGeometry(QtCore.QRect(260, 305, 72, 15))
        self.labelStaffNo.setObjectName("labelStaffNo")
        self.lineEditSupNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSupNo.setEnabled(True)
        self.lineEditSupNo.setGeometry(QtCore.QRect(420, 200, 113, 21))
        self.lineEditSupNo.setObjectName("lineEditSupNo")
        self.pushButtonReturn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReturn.setGeometry(QtCore.QRect(490, 430, 40, 40))
        self.pushButtonReturn.setText("")
        self.pushButtonReturn.setObjectName("pushButtonReturn")
        self.labelCarNum = QtWidgets.QLabel(self.centralwidget)
        self.labelCarNum.setEnabled(True)
        self.labelCarNum.setGeometry(QtCore.QRect(260, 255, 72, 15))
        self.labelCarNum.setObjectName("labelCarNum")
        self.lineEditTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTotal.setGeometry(QtCore.QRect(420, 350, 113, 21))
        self.lineEditTotal.setObjectName("lineEditTotal")
        self.labelTotal = QtWidgets.QLabel(self.centralwidget)
        self.labelTotal.setGeometry(QtCore.QRect(260, 355, 72, 15))
        self.labelTotal.setObjectName("labelTotal")
        self.lineEditCarNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCarNum.setEnabled(True)
        self.lineEditCarNum.setGeometry(QtCore.QRect(420, 250, 113, 21))
        self.lineEditCarNum.setObjectName("lineEditCarNum")
        self.lineEditStaffNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditStaffNo.setGeometry(QtCore.QRect(420, 300, 113, 21))
        self.lineEditStaffNo.setObjectName("lineEditStaffNo")
        self.labelSupNo = QtWidgets.QLabel(self.centralwidget)
        self.labelSupNo.setEnabled(True)
        self.labelSupNo.setGeometry(QtCore.QRect(260, 205, 72, 15))
        self.labelSupNo.setObjectName("labelSupNo")
        self.labelCarNo = QtWidgets.QLabel(self.centralwidget)
        self.labelCarNo.setEnabled(True)
        self.labelCarNo.setGeometry(QtCore.QRect(260, 155, 72, 15))
        self.labelCarNo.setObjectName("labelCarNo")
        self.lineEditCarNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCarNo.setEnabled(True)
        self.lineEditCarNo.setGeometry(QtCore.QRect(420, 150, 113, 21))
        self.lineEditCarNo.setObjectName("lineEditCarNo")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 70, 191, 51))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 490, 72, 15))
        self.label.setStyleSheet("font: 10pt \"新宋体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 490, 72, 15))
        self.label_2.setStyleSheet("font: 10pt \"新宋体\";")
        self.label_2.setObjectName("label_2")
        self.pushButtonOK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOK.setGeometry(QtCore.QRect(270, 430, 40, 40))
        self.pushButtonOK.setText("")
        self.pushButtonOK.setObjectName("pushButtonOK")
        carPurchase.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(carPurchase)
        self.statusbar.setObjectName("statusbar")
        carPurchase.setStatusBar(self.statusbar)

        self.retranslateUi(carPurchase)
        QtCore.QMetaObject.connectSlotsByName(carPurchase)

    def retranslateUi(self, carPurchase):
        _translate = QtCore.QCoreApplication.translate
        carPurchase.setWindowTitle(_translate("carPurchase", "汽车采购"))
        self.labelStaffNo.setText(_translate("carPurchase", "员工号"))
        self.labelCarNum.setText(_translate("carPurchase", "汽车数量"))
        self.labelTotal.setText(_translate("carPurchase", "汽车总价"))
        self.labelSupNo.setText(_translate("carPurchase", "供应商编号"))
        self.labelCarNo.setText(_translate("carPurchase", "汽车编号"))
        self.label_7.setText(_translate("carPurchase", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">汽车采购</span></p></body></html>"))
        self.label.setText(_translate("carPurchase", "确定"))
        self.label_2.setText(_translate("carPurchase", "返回"))

