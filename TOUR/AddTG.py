from UI.添加旅行团 import *
from PyQt5 import QtCore, QtWidgets, QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox
import pymssql
import random

class groupAdd(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(groupAdd, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.results)
        self.setObjectName("AddTG")
        self.setStyleSheet(
            "#AddTG{border-image:url(pic/6.jpg);}"
            "#pushButton{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButton:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )
    def results(self):
        groupDate = self.lineEditDate.text()
        transNo = self.lineEditTranspNo.text()
        hotelNo = self.lineEditHotelNo.text()
        guideNo = self.lineEditGuideNo.text()
        routeNo = self.lineEditRouteNo.text()
        randomOrder = 'TG_' + str(transNo)[-2:] + str(hotelNo)[-3:] +  str(random.randint(1000, 9999))
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "Travel_Agency"
        conn5 = pymssql.connect(server, user, password, database)
        tour_group_add = conn5.cursor()
        tour_group_add.execute("insert into tour_group values(%s,%s,%s,%s,%s,0,%s)",(randomOrder,hotelNo,routeNo,guideNo,transNo,groupDate) )
        QMessageBox.information(self, "   ", "ADDING ACCOMPLISHED！")
        conn5.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cI = groupAdd()
    cI.show()
    sys.exit(app.exec())