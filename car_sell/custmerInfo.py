from UI.顾客信息 import *
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from purchase import *
from operation import *
from infoRegister import *
from PyQt5.QtWidgets import QMessageBox
import sys
import pymssql
class custmerInfo(QMainWindow,Ui_MainWindowCustmerInfo):
    def __init__(self,parent=None):
        super(custmerInfo,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonRegister.clicked.connect(self.toRegister)
        self.pushButtonRegister.clicked.connect(self.hide)
        self.pushButtonSearch.clicked.connect(self.results)

        self.setObjectName("CustmerInfoWindow")
        self.setStyleSheet(
            "#CustmerInfoWindow{border-image:url(Pics/road3.jpg);}"
            "#pushButtonSearch{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonRegister{border-radius:100px;background-image:url(icon/add.png);}"
            "#pushButtonSearch:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonRegister:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )


    def toRegister(self):
        self.toRegister=infoInput()
        self.toRegister.show()

    def results(self):
        custmerName = self.lineEditSearch.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "car_sale"
        conn2 = pymssql.connect(server, user, password, database)
        cursor_custmer_info = conn2.cursor()
        cursor_custmer_info.execute("select c_id,c_name,c_gender,tele from customer where customer.c_name=%s",custmerName)
        rows = cursor_custmer_info.fetchall()
        QMessageBox.information(self, "   ", "SELECTING ACCOMPLISHED！")
        row = cursor_custmer_info.rowcount  # 取得记录个数，用于设置表格的行数
        vol = len(rows[0])  # 取得字段数，用于设置表格的列数

        self.tableWidgetResult.setRowCount(row)
        self.tableWidgetResult.setColumnCount(vol)

        for i in range(row):
            for j in range(vol):
                temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.tableWidgetResult.setItem(i, j, data)
if __name__=="__main__":
    app=QApplication(sys.argv)
    cI=custmerInfo()
    cI.show()
    sys.exit(app.exec())