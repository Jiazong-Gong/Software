from UI.员工登录 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
from operation import *

import pymssql
class login(QMainWindow,Ui_staffLogin):
    def __init__(self,parent=None):
        super(login,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonClear.clicked.connect(self.clearLine)
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.pushButtonOK.clicked.connect(self.check)

        self.setObjectName("LoginWindow")
        self.setStyleSheet(
            "#LoginWindow{border-image:url(Pics/plane.jpg);}"
            "#pushButtonOK{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonClear{border-radius:100px;background-image:url(icon/clear.png);}"
            "#pushButtonClear:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonOK:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )

    def clearLine(self):
        self.lineEditStaff.clear()
        self.lineEditPassword.clear()

    def paint(self,event):
        painter=QPainter(self)
        pic=QPixmap("D:\Pics\car1")
        painter.drawPixmap(self.rect(),pic)
    def check(self):

        acc = self.lineEditStaff.text()
        pss = self.lineEditPassword.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "car_sale"
        conn7 = pymssql.connect(server, user, password, database)
        cursor_to_login = conn7.cursor()
        cursor_to_login.execute("select password from login where account=%s", acc)
        row = cursor_to_login.fetchone()
        if acc==row :
            self.close
            QMessageBox.information(self, "  ", "Successfully login！")
            self.a = oper()

            self.a.show()

        else:
            QMessageBox.information(self, "ERROR", "TRY AGAIN！")
if __name__=="__main__":
    app=QApplication(sys.argv)
    login1=login()
    login1.show()
    sys.exit(app.exec())