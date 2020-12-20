from UI.添加酒店 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
import pymssql
import random
class hotelAdd(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(hotelAdd, self).__init__(parent)
        self.setupUi(self)

        self.pushButtonAdd.clicked.connect(self.results)
        self.setObjectName("AddHotel")
        self.setStyleSheet(
            "#AddHotel{border-image:url(pic/2.jpg);}"
            "#pushButtonAdd{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonAdd:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )
    def results(self):
        hotelTele=self.lineEditTele.text()
        hotelName=self.lineEditHotelName.text()
        hotelCity=self.lineEditCity.text()
        hotelType=self.lineEditType.text()
        hotelMax=self.lineEditMax.text()
        hotelPrice=self.lineEditPrice.text()
        randomOrder = 'H_' + str(hotelName)[-2:] + str(hotelMax)[-3:] + str(hotelTele)[:] + str(random.randint(1000, 9999))
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "Travel_Agency"
        conn10 = pymssql.connect(server, user, password, database)
        hotel_add = conn10.cursor()
        hotel_add.execute("insert into hotel values(%s,%s,%s,%s,%s,%s,%s)",(randomOrder,hotelName,hotelTele,hotelCity,hotelType,hotelMax,hotelPrice) )
        QMessageBox.information(self, "   ", "ADDING ACCOMPLISHED！")
        conn10.commit()

if __name__=="__main__":
    app=QApplication(sys.argv)
    cI=hotelAdd()
    cI.show()
    sys.exit(app.exec())