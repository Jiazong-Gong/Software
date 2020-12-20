# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '添加旅行团.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(717, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 90, 72, 15))
        self.label.setObjectName("label")
        self.lineEditRouteNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRouteNo.setGeometry(QtCore.QRect(360, 90, 113, 21))
        self.lineEditRouteNo.setObjectName("lineEditRouteNo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 170, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEditGuideNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditGuideNo.setGeometry(QtCore.QRect(360, 170, 113, 21))
        self.lineEditGuideNo.setObjectName("lineEditGuideNo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 240, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEditHotelNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditHotelNo.setGeometry(QtCore.QRect(360, 240, 113, 21))
        self.lineEditHotelNo.setObjectName("lineEditHotelNo")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 310, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEditTranspNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTranspNo.setGeometry(QtCore.QRect(360, 310, 113, 21))
        self.lineEditTranspNo.setObjectName("lineEditTranspNo")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 380, 72, 15))
        self.label_5.setObjectName("label_5")
        self.lineEditDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDate.setGeometry(QtCore.QRect(360, 380, 113, 21))
        self.lineEditDate.setObjectName("lineEditDate")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 440, 40, 40))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 510, 81, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "添加旅行团"))
        self.label.setText(_translate("MainWindow", "线路编号"))
        self.label_2.setText(_translate("MainWindow", "导游编号"))
        self.label_3.setText(_translate("MainWindow", "酒店编号"))
        self.label_4.setText(_translate("MainWindow", "出行方式编号"))
        self.label_5.setText(_translate("MainWindow", "出发时间"))
        self.label_6.setText(_translate("MainWindow", "添加旅行团"))

