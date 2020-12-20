from UI.顾客信息登记 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from custmerInfo import *
from PyQt5.QtWidgets import QMessageBox
import pymssql
class infoInput(QMainWindow,Ui_MainWindowCustmerInfoRegister):
    def __init__(self,parent=None):
        super(infoInput,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonOK.clicked.connect(self.conn)
        self.pushButtonOK.clicked.connect(self.hide)
        self.pushButtonOK.clicked.connect(self.intoSqlCustmer)
        self.pushButtonReinput.clicked.connect(self.clearAll)

        self.setObjectName("IntoRegisterWindow")
        self.setStyleSheet(
            "#IntoRegisterWindow{border-image:url(Pics/road.jpg);}"
            "#pushButtonOK{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonReinput{border-radius:100px;background-image:url(icon/clear.png);}"
            "#pushButtonOK:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonReinput:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )

    def conn(self):
        self.conn=custmerInfo()
        self.conn.show()

    def clearAll(self):
        self.lineEditCustmerTele.clear()
        self.lineEditCustmerGender.clear()
        self.lineEditCustmerID.clear()
        self.lineEditCustmerName.clear()

    def intoSqlCustmer(self):
        custmerName=self.lineEditCustmerName.text()
        custmerNo=self.lineEditCustmerID.text()
        custmerGender=self.lineEditCustmerGender.text()
        custmerTele=self.lineEditCustmerTele.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "car_sale"
        conn4 = pymssql.connect(server, user, password, database)
        cursor_custmer_register = conn4.cursor()
        cursor_custmer_register.execute("insert into customer values(%s,%s,%s,%s)",(custmerNo,custmerName,custmerGender,custmerTele))
        conn4.commit()
        QMessageBox.information(self, "  ", "REGISTER ACCOMPLISHED！")
if __name__=="__main__":
    app=QApplication(sys.argv)
    infoInput1=infoInput()
    infoInput1.show()
    sys.exit(app.exec())