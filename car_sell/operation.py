from UI.员工操作界面 import *
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from purchase import *
from carLib import *
from custmerInfo import *
from carSell import *
from supplyInfo import *
from orderDetail import *
from PyQt5.QtWidgets import QMessageBox
import sys
class oper(QMainWindow,Ui_operationWindow):
    def __init__(self, parent=None):
        super(oper,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonCarPurchase.clicked.connect(self.con2)
        self.pushButtonCarLib.clicked.connect(self.con3)
        self.pushButtonCustmerInfo.clicked.connect(self.con4)
        self.pushButtonSupInfo.clicked.connect(self.con5)
        self.pushButtonCarSell.clicked.connect(self.con6)
        self.pushButtonOrderDetail.clicked.connect(self.con7)
        self.pushButtonUpdatePic.clicked.connect(self.con8)
        self.labelPic.setPixmap(QPixmap("Pics/pic1.jpg"))
        self.labelPic.setScaledContents(True)
        self.labelID.setScaledContents(True)
        self.labelName.setScaledContents(True)
        self.labelID.setText("编号"+"S005")
        self.labelName.setText("姓名"+"Sakery")
        self.setObjectName("OperationWindow")
        self.setStyleSheet(
            "#OperationWindow{border-image:url(Pics/road1.jpg);}"
            "#pushButtonOrderDetail{border-radius:100px;background-image:url(icon/icon7.png);}"
            "#pushButtonCarPurchase{border-radius:100px;background-image:url(icon/icon8.png);}"
            "#pushButtonCarLib{border-radius:100px;background-image:url(icon/icon3.png);}"
            "#pushButtonCustmerInfo{border-radius:100px;background-image:url(icon/icon4.png);}"
            "#pushButtonCarSell{border-radius:100px;background-image:url(icon/icon10.png);}"
            "#pushButtonSupInfo{border-radius:100px;background-image:url(icon/icon6.png);}"
            "#pushButtonUpdatePic{border-radius:100px;background-image:url(icon/updatePic.png);}"
            "#pushButtonUpdatePic:hover{border-radius:100px;background-image:url(icon/change.png);}"
            "#pushButtonOrderDetail:hover{border-radius:100px;background-image:url(icon/speed.png);}"
            "#pushButtonCarPurchase:hover{border-radius:100px;background-image:url(icon/speed.png);}"
            "#pushButtonCarLib:hover{border-radius:100px;background-image:url(icon/speed.png);}"
            "#pushButtonCustmerInfo:hover{border-radius:100px;background-image:url(icon/speed.png);}"
            "#pushButtonCarSell:hover{border-radius:100px;background-image:url(icon/speed.png);}"
            "#pushButtonSupInfo:hover{border-radius:100px;background-image:url(icon/speed.png);}"
        )

    def con2(self):
        self.CarPur=purchaseCar()
        self.CarPur.show()

    def con3(self):
        self.carLib=carLib()
        self.carLib.show()

    def con4(self):
        self.custmerInfo=custmerInfo()
        self.custmerInfo.show()

    def con5(self):
        self.supplyInfo=supplyInfo()
        self.supplyInfo.show()

    def con6(self):
        self.carSell=carSell()
        self.carSell.show()

    def con7(self):
        self.order=orderDetail()
        self.order.show()

    def con8(self):
        fileName, filetype = QFileDialog.getOpenFileName(self,"选择头像","F:/untitled5/Pics","图片文件(*.jpg);")

        if fileName != None:
            self.labelPic.setPixmap(QPixmap(fileName))
if __name__=="__main__":
    app=QApplication(sys.argv)
    op=oper()
    op.show()
    sys.exit(app.exec())


