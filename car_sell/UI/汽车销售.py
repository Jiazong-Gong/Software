# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '汽车销售.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowCarSell(object):
    def setupUi(self, MainWindowCarSell):
        MainWindowCarSell.setObjectName("MainWindowCarSell")
        MainWindowCarSell.resize(718, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindowCarSell)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCarNo = QtWidgets.QLabel(self.centralwidget)
        self.labelCarNo.setGeometry(QtCore.QRect(190, 70, 72, 15))
        self.labelCarNo.setObjectName("labelCarNo")
        self.labelCarNum = QtWidgets.QLabel(self.centralwidget)
        self.labelCarNum.setGeometry(QtCore.QRect(190, 120, 72, 15))
        self.labelCarNum.setObjectName("labelCarNum")
        self.labelCustmerNo = QtWidgets.QLabel(self.centralwidget)
        self.labelCustmerNo.setGeometry(QtCore.QRect(190, 170, 72, 15))
        self.labelCustmerNo.setObjectName("labelCustmerNo")
        self.labelCustmerName = QtWidgets.QLabel(self.centralwidget)
        self.labelCustmerName.setGeometry(QtCore.QRect(190, 220, 72, 15))
        self.labelCustmerName.setObjectName("labelCustmerName")
        self.labelStaffNo = QtWidgets.QLabel(self.centralwidget)
        self.labelStaffNo.setGeometry(QtCore.QRect(190, 320, 72, 15))
        self.labelStaffNo.setObjectName("labelStaffNo")
        self.pushButtonOK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOK.setGeometry(QtCore.QRect(210, 440, 40, 40))
        self.pushButtonOK.setText("")
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonReturn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReturn.setGeometry(QtCore.QRect(440, 440, 40, 40))
        self.pushButtonReturn.setText("")
        self.pushButtonReturn.setObjectName("pushButtonReturn")
        self.labelTotal = QtWidgets.QLabel(self.centralwidget)
        self.labelTotal.setGeometry(QtCore.QRect(190, 370, 72, 15))
        self.labelTotal.setObjectName("labelTotal")
        self.lineEditCarNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCarNo.setGeometry(QtCore.QRect(420, 70, 113, 21))
        self.lineEditCarNo.setObjectName("lineEditCarNo")
        self.lineEditCustmerNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCustmerNo.setGeometry(QtCore.QRect(420, 170, 113, 21))
        self.lineEditCustmerNo.setObjectName("lineEditCustmerNo")
        self.lineEditCarNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCarNum.setGeometry(QtCore.QRect(420, 120, 113, 21))
        self.lineEditCarNum.setObjectName("lineEditCarNum")
        self.lineEditCustmerName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCustmerName.setGeometry(QtCore.QRect(420, 220, 113, 21))
        self.lineEditCustmerName.setObjectName("lineEditCustmerName")
        self.lineEditCustmerTele = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCustmerTele.setGeometry(QtCore.QRect(420, 270, 113, 21))
        self.lineEditCustmerTele.setObjectName("lineEditCustmerTele")
        self.lineEditStaffNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditStaffNo.setGeometry(QtCore.QRect(420, 320, 113, 21))
        self.lineEditStaffNo.setObjectName("lineEditStaffNo")
        self.labelCustmerTele = QtWidgets.QLabel(self.centralwidget)
        self.labelCustmerTele.setGeometry(QtCore.QRect(190, 270, 72, 15))
        self.labelCustmerTele.setObjectName("labelCustmerTele")
        self.lineEditTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTotal.setGeometry(QtCore.QRect(420, 370, 113, 21))
        self.lineEditTotal.setObjectName("lineEditTotal")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 500, 72, 15))
        self.label.setStyleSheet("font: 10pt \"新宋体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 500, 72, 15))
        self.label_2.setStyleSheet("font: 10pt \"新宋体\";")
        self.label_2.setObjectName("label_2")
        MainWindowCarSell.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowCarSell)
        self.statusbar.setObjectName("statusbar")
        MainWindowCarSell.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowCarSell)
        QtCore.QMetaObject.connectSlotsByName(MainWindowCarSell)

    def retranslateUi(self, MainWindowCarSell):
        _translate = QtCore.QCoreApplication.translate
        MainWindowCarSell.setWindowTitle(_translate("MainWindowCarSell", "汽车销售"))
        self.labelCarNo.setText(_translate("MainWindowCarSell", "汽车编号"))
        self.labelCarNum.setText(_translate("MainWindowCarSell", "数量"))
        self.labelCustmerNo.setText(_translate("MainWindowCarSell", "顾客编号"))
        self.labelCustmerName.setText(_translate("MainWindowCarSell", "顾客姓名"))
        self.labelStaffNo.setText(_translate("MainWindowCarSell", "员工编号"))
        self.labelTotal.setText(_translate("MainWindowCarSell", "总价"))
        self.labelCustmerTele.setText(_translate("MainWindowCarSell", "顾客电话"))
        self.label.setText(_translate("MainWindowCarSell", "确定"))
        self.label_2.setText(_translate("MainWindowCarSell", "返回"))

