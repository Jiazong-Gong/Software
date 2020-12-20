from UI.游客信息录入 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
import pymssql
import random
class touristAdd(QMainWindow,Ui_MainWindowTourists):
    def __init__(self,parent=None):
        super(touristAdd,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonOK.clicked.connect(self.results)
        self.setObjectName("AddTourist")
        self.setStyleSheet(
            "#AddTourist{border-image:url(pic/11.jpg);}"
            "#pushButtonOK{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonOK:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )
    def results(self):
        tName = self.lineEditName.text()
        tGender=self.lineEditGender.text()
        tAge=self.lineEditAge.text()
        tTele=self.lineEditTele.text()
        tTourG=self.lineEditTourGroup.text()
        randomOrder = 'T_' + str(tTele) + str(tAge) + str(tTourG) + str(random.randint(1000, 9999))
        print(randomOrder,tName,tGender,tTele,tAge,tTourG)
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "Travel_Agency"
        conn2 = pymssql.connect(server, user, password, database)
        add_tourist = conn2.cursor()
        add_tourist.execute("insert into tourists values(%s,%s,%s,%s,%s,%s)",(randomOrder,tName,tGender,tTele,tAge,tTourG) )
        QMessageBox.information(self, "   ", "ADDING ACCOMPLISHED！")
        conn2.commit()


if __name__=="__main__":
    app=QApplication(sys.argv)
    cI=touristAdd()
    cI.show()
    sys.exit(app.exec())