from UI.供应商信息 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
from operation import *
from PyQt5.QtWidgets import QMessageBox
import pymssql
class supplyInfo(QMainWindow,Ui_MainWindowSupply):
    def __init__(self,parent=None):
        super(supplyInfo,self).__init__(parent)
        self.setupUi(self)


        self.pushButtonSupplySearch.clicked.connect(self.results)
        self.pushButtonDelete.clicked.connect(self.deleteOne)

        self.setObjectName("SupplyInfoWindow")
        self.setStyleSheet(
            "#SupplyInfoWindow{border-image:url(Pics/coast.jpg);}"
            "#pushButtonSupplySearch{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonDelete{border-radius:100px;background-image:url(icon/delete.png);}"
            "#pushButtonSupplySearch:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonDelete:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )



    def results(self):
        supplyName=self.lineEditSupplyNo.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "car_sale"
        conn3 = pymssql.connect(server, user, password, database)
        cursor_supply_info = conn3.cursor()
        cursor_supply_info.execute("select pr_id,pr_name,p_tele from prv where pr_id=%s",supplyName)
        rows = cursor_supply_info.fetchall()
        QMessageBox.information(self, "   ", "SELECTING ACCOMPLISHED！")
        row = cursor_supply_info.rowcount  # 取得记录个数，用于设置表格的行数
        vol = len(rows[0])  # 取得字段数，用于设置表格的列数


        self.tableWidgetSupplyInfo.setRowCount(row)
        self.tableWidgetSupplyInfo.setColumnCount(vol)

        for i in range(row):
            for j in range(vol):
                temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.tableWidgetSupplyInfo.setItem(i, j, data)

    def deleteOne(self):
        supplyName=self.lineEditDelete.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "car_sale"
        conn8 = pymssql.connect(server, user, password, database)
        cursor_delete_supply = conn8.cursor()
        cursor_delete_supply.execute("delete from prv where pr_id=%s", supplyName)
        conn8.commit()
        QMessageBox.information(self, "   ", "DELETING ACCOMPLISHED！")

if __name__=="__main__":
    app=QApplication(sys.argv)
    cI=supplyInfo()
    cI.show()
    sys.exit(app.exec())