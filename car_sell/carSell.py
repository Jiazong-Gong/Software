from UI.汽车销售 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
from operation import *
from PyQt5.QtWidgets import QMessageBox
import math
import random
class carSell(QMainWindow,Ui_MainWindowCarSell):
    def __init__(self, parent=None):
        super(carSell,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonReturn.clicked.connect(self.toOper)
        self.pushButtonReturn.clicked.connect(self.hide)
        self.pushButtonOK.clicked.connect(self.toSell)

        self.setObjectName("CarSellWindow")
        self.setStyleSheet(
            "#CarSellWindow{border-image:url(Pics/sky.jpg);}"
            "#pushButtonReturn{border-radius:100px;background-image:url(icon/return.png);}"
            "#pushButtonOK{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonReturn:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonOK:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )



    def toOper(self):
        self.toOper=oper()
        self.toOper.show()


    def toSell(self):
        carNo=self.lineEditCarNo.text()
        staffNo=self.lineEditStaffNo.text()
        custmerNo=self.lineEditCustmerNo.text()
        carNum=self.lineEditCarNum.text()
        carTotal=self.lineEditTotal.text()
        randomOrder='O_'+str(carNo)[-2:]+str(staffNo)[-3:]+str(carNum)[:]+str(random.randint(1000, 9999))
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "car_sale"
        conn6 = pymssql.connect(server, user, password, database)
        cursor_sell_cars = conn6.cursor()
        cursor_sell_cars.execute("insert into order_detail values(%s,getdate(),%s,%s,%s,%s,%s)",(randomOrder,carNo, staffNo,custmerNo,carNum,carTotal))
        # cursor_sell_cars.execute("update cars set left_num=left_num-%d where car_id=%s",carNum,carNo)
        conn6.commit()
        QMessageBox.information(self, "   ", "SELLING ACCOMPLISHED！")
if __name__=="__main__":
    app=QApplication(sys.argv)
    cS=carSell()
    cS.show()
    sys.exit(app.exec())