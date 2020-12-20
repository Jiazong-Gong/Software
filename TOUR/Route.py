from ChangeRoute import *
from UI.线路管理 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox
import pymssql
class routeInfo(QMainWindow,Ui_MainWindowRoute):
    def __init__(self,parent=None):
        super(routeInfo, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.results)
        self.pushButtonAdd.clicked.connect(self.add)
        self.setObjectName("Route")
        self.setStyleSheet(
            "#Route{border-image:url(pic/4.jpg);}"
            "#pushButton{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButton:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )
    def add(self):
        self.aa=routeAdd()
        self.aa.show()
    def results(self):
        routeName = self.lineEdit_3.text()
        if routeName=='A':
            server = "JASONK"
            user = "sa"
            password = "123456"
            database = "Travel_Agency"
            conn3 = pymssql.connect(server, user, password, database)
            route_info_search = conn3.cursor()
            route_info_search.execute("select * from rousight where r_id LIKE 'A___'")
            rows = route_info_search.fetchall()

            row = route_info_search.rowcount  # 取得记录个数，用于设置表格的行数
            if row == 0:
                QMessageBox.information(self, "   ", "NO RESULTS！")
            else:
                QMessageBox.information(self, "   ", "SELECTING ACCOMPLISHED！")
                vol = len(rows[0])  # 取得字段数，用于设置表格的列数

                self.tableWidget.setRowCount(row)
                self.tableWidget.setColumnCount(vol)

                for i in range(row):
                    for j in range(vol):
                        temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.tableWidget.setItem(i, j, data)
        elif routeName=='B':
            server = "JASONK"
            user = "sa"
            password = "123456"
            database = "Travel_Agency"
            conn3 = pymssql.connect(server, user, password, database)
            route_info_search = conn3.cursor()
            route_info_search.execute("select * from rousight where r_id LIKE 'B___'")
            rows = route_info_search.fetchall()

            row = route_info_search.rowcount  # 取得记录个数，用于设置表格的行数
            if row == 0:
                QMessageBox.information(self, "   ", "NO RESULTS！")
            else:
                QMessageBox.information(self, "   ", "SELECTING ACCOMPLISHED！")
                vol = len(rows[0])  # 取得字段数，用于设置表格的列数

                self.tableWidget.setRowCount(row)
                self.tableWidget.setColumnCount(vol)

                for i in range(row):
                    for j in range(vol):
                        temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.tableWidget.setItem(i, j, data)
        else:
            QMessageBox.information(self, "   ", "NO EXISTING ROUTE！")

if __name__=="__main__":
    app=QApplication(sys.argv)
    cI=routeInfo()
    cI.show()
    sys.exit(app.exec())