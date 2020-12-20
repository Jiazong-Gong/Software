from UI.库存查询 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
from operation import *
from purchase import *
from PyQt5.QtWidgets import QMessageBox
import pymssql
class carLib(QMainWindow,Ui_CarLib):
    def __init__(self,parent=None):
        super(carLib,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonSearch.clicked.connect(self.results)
        self.pushButtonDelete.clicked.connect(self.deleteOne)

        self.setObjectName("CarLibWindow")
        self.setStyleSheet("#CarLibWindow{border-image:url(Pics/city.jpg);}")
        self.setStyleSheet(
            "#CarLibWindow{border-image:url(Pics/city.jpg);}"
            "#pushButtonSearch{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonDelete{border-radius:100px;background-image:url(icon/delete.png);}"
            "#pushButtonDelete:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonSearch:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )

    def results(self):
        carBrand=self.lineEditBrandSearch.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "car_sale"
        conn1 = pymssql.connect(server, user, password, database)
        cursor_car_lib = conn1.cursor()
        cursor_car_lib.execute("select car_id,car_name,price,left_num from cars where cars.brand=%s", carBrand)
        rows = cursor_car_lib.fetchall()
        QMessageBox.information(self, "   ", "SELECTING ACCOMPLISHED！")
        row = cursor_car_lib.rowcount  # 取得记录个数，用于设置表格的行数
        vol = len(rows[0])  # 取得字段数，用于设置表格的列数
        cursor_car_lib.close()
        conn1.close()

        self.tableWidgetLib.setRowCount(row)
        self.tableWidgetLib.setColumnCount(vol)

        for i in range(row):
            for j in range(vol):
                temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.tableWidgetLib.setItem(i, j, data)
    def deleteOne(self):
        carName=self.lineEditDelete.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "car_sale"
        conn9 = pymssql.connect(server, user, password, database)
        cursor_delete_car = conn9.cursor()
        cursor_delete_car.execute("delete from cars where car_name=%s", carName)
        conn9.commit()
        QMessageBox.information(self, "   ", "DELETING ACCOMPLISHED！")
if __name__=="__main__":
    app=QApplication(sys.argv)
    cl=carLib()
    cl.show()
    sys.exit(app.exec())