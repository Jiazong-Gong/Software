from UI.添加导游 import *
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

class guideAdd(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(guideAdd, self).__init__(parent)
        self.setupUi(self)

        self.pushButtonAdd.clicked.connect(self.add)
        self.setObjectName("AddGuide")
        self.setStyleSheet(
            "#AddGuide{border-image:url(pic/1.jpg);}"
            "#pushButtonAdd{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonAdd:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )
    def add(self):
        guideName = self.lineEditName.text()
        guideTele=self.lineEditTele.text()
        guideGender=self.lineEditGender.text()
        guideAge=self.lineEditAge.text()
        randomOrder = 'G_' + str(guideAge)[-2:] + str(guideTele)[-3:] + str(random.randint(1000, 9999))
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "Travel_Agency"
        conn1 = pymssql.connect(server, user, password, database)
        guide_info_search = conn1.cursor()
        guide_info_search.execute("insert into guide values(%s,%s,%s,%s,%s)", (randomOrder,guideName,guideTele,guideGender,guideAge))
        QMessageBox.information(self, "   ", "ADDING ACCOMPLISHED！")
        conn1.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cI = guideAdd()
    cI.show()
    sys.exit(app.exec())