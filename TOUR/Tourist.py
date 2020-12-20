from AddTourist import *
from UI.游客信息 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox
import pymssql

class touristsInfo(QMainWindow,Ui_MainWindowTourists):
    def __init__(self,parent=None):
        super(touristsInfo,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonSearch.clicked.connect(self.results)
        self.pushButtonRegister.clicked.connect(self.toRegister)
        self.setObjectName("Tourist")
        self.setStyleSheet(
            "#Tourist{border-image:url(pic/7.jpg);}"
            "#pushButtonSearch{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonRegister{border-radius:100px;background-image:url(icon/add.png);}"
            "#pushButtonSearch:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonRegister:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )
    def toRegister(self):
        self.tt=touristAdd()
        self.tt.show()
    def results(self):
        touristName = self.lineEditName.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "Travel_Agency"
        conn3 = pymssql.connect(server, user, password, database)
        tourist_info_search = conn3.cursor()
        tourist_info_search.execute("select * from tourists where t_name=%s", touristName)
        rows = tourist_info_search.fetchall()

        row = tourist_info_search.rowcount  # 取得记录个数，用于设置表格的行数
        if row==0:
            QMessageBox.information(self, "   ", "NO RESULTS！")
        else:
            QMessageBox.information(self, "   ", "SELECTING ACCOMPLISHED！")
            vol = len(rows[0])  # 取得字段数，用于设置表格的列数

            self.tableWidgetResults.setRowCount(row)
            self.tableWidgetResults.setColumnCount(vol)

            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.tableWidgetResults.setItem(i, j, data)


if __name__=="__main__":
    app=QApplication(sys.argv)
    cI=touristsInfo()
    cI.show()
    sys.exit(app.exec())