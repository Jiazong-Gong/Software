from UI.订单信息 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
from operation import *
from purchase import *
import pymssql
class orderDetail(QMainWindow,Ui_MainWindowOrderSearch):
    def __init__(self,parent=None):
        super(orderDetail,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonSearch.clicked.connect(self.results)

        self.setObjectName("OrderDetailWindow")
        self.setStyleSheet(
            "#OrderDetailWindow{border-image:url(Pics/ocean.jpg);}"
            "#pushButtonSearch{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonSearch:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )


    def results(self):
        self.type11=self.comboBoxType.currentText()
        type1=self.lineEditType.text()
        if self.type11 == "员工号":
            server = "JASONK"
            user = "sa"
            password = "123456"
            database = "car_sale"
            conn5 = pymssql.connect(server, user, password, database)
            cursor_order_detail = conn5.cursor()
            cursor_order_detail.execute("select o_id,o_date,s_id,car_id,c_id,number,total_price from order_detail where s_id=%s", type1)
            rows = cursor_order_detail.fetchall()
            QMessageBox.information(self, "   ", "SELECTING ACCOMPLISHED！")
            row = cursor_order_detail.rowcount  # 取得记录个数，用于设置表格的行数
            vol = len(rows[0])  # 取得字段数，用于设置表格的列数

            self.tableWidgetResults.setRowCount(row)
            self.tableWidgetResults.setColumnCount(vol)

            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.tableWidgetResults.setItem(i, j, data)
        elif self.type11 == "订单号":
            server = "JASONK"
            user = "sa"
            password = "123456"
            database = "car_sale"
            conn5 = pymssql.connect(server, user, password, database)
            cursor_order_detail = conn5.cursor()
            cursor_order_detail.execute("select o_id,o_date,s_id,car_id,c_id,number,total_price from order_detail where o_id=%s", type1)
            rows = cursor_order_detail.fetchall()
            QMessageBox.information(self, "   ", "SELECTING ACCOMPLISHED！")
            row = cursor_order_detail.rowcount  # 取得记录个数，用于设置表格的行数
            vol = len(rows[0])  # 取得字段数，用于设置表格的列数


            self.tableWidgetResults.setRowCount(row)
            self.tableWidgetResults.setColumnCount(vol)

            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.tableWidgetResults.setItem(i, j, data)
        else:
            server = "JASONK"
            user = "sa"
            password = "123456"
            database = "car_sale"
            conn5 = pymssql.connect(server, user, password, database)
            cursor_order_detail = conn5.cursor()
            cursor_order_detail.execute("select o_id,o_date,s_id,car_id,c_id,number,total_price from order_detail where c_id=%s", type1)
            rows = cursor_order_detail.fetchall()
            QMessageBox.information(self, "   ", "SELECTING ACCOMPLISHED！")
            row = cursor_order_detail.rowcount  # 取得记录个数，用于设置表格的行数
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
    oD=orderDetail()
    oD.show()
    sys.exit(app.exec())