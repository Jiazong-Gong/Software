from UI.购买 import *
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from operation import *
from PyQt5.QtWidgets import QMessageBox
import pymssql
import math
import random
class purchaseCar(QMainWindow,Ui_carPurchase):
    def __init__(self,parent=None):
        super(purchaseCar,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonReturn.clicked.connect(self.toOper)
        self.pushButtonReturn.clicked.connect(self.hide)
        self.pushButtonOK.clicked.connect(self.intoCar)

        self.setObjectName("PurchaseWindow")
        self.setStyleSheet(
            "#PurchaseWindow{border-image:url(Pics/island.jpg);}"
            "#pushButtonReturn:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonOK:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonOK{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonReturn{border-radius:100px;background-image:url(icon/return.png);}"
        )

    def toOper(self):
        self.toOper=oper()
        self.toOper.show()

    def intoCar(self):
        carNo=self.lineEditCarNo.text()
        supplyNo=self.lineEditSupNo.text()
        carNum=self.lineEditCarNum.text()
        staffNo=self.lineEditStaffNo.text()
        total=self.lineEditTotal.text()

        randomNum='p_'+str(carNo)[-3:]+str(supplyNo)[-2:]+str(carNum)[:]+str(random.randint(1000, 9999))
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "car_sale"
        conn6 = pymssql.connect(server, user, password, database)
        cursor_purchase_car = conn6.cursor()
        cursor_purchase_car.execute("insert into purchase values(%s,%s,%s,%s,&s,%s,%s,getdate())",(randomNum,supplyNo,carNo,staffNo,carNum,total))
        # cursor_purchase_car.execute("update cars set left_num=left_num+%d where car_id=%s",carNum,carNo)
        conn6.commit()
        QMessageBox.information(self, "   ", "PURCHASING ACCOMPLISHED！")
if __name__=="__main__":
    app=QApplication(sys.argv)
    pC1=purchaseCar()
    pC1.show()
    sys.exit(app.exec())