from UI.出行方式信息 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox
import pymssql
class transInfo(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(transInfo, self).__init__(parent)
        self.setupUi(self)

        self.pushButtonSearch.clicked.connect(self.results)
        self.setObjectName("TransInfo")
        self.setStyleSheet(
            "#TransInfo{border-image:url(pic/2.jpg);}"
            "#pushButtonSearch{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonSearch:hover{border-radius:100px;background-image:url(icon/hover.png);}"
        )
    def results(self):
        transNo = self.lineEditTransp.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "Travel_Agency"
        conn9 = pymssql.connect(server, user, password, database)
        trans_info_search = conn9.cursor()
        trans_info_search.execute("select * from transp where trans_type=%s",transNo )
        rows = trans_info_search.fetchall()

        row = trans_info_search.rowcount  # 取得记录个数，用于设置表格的行数
        if row==0:
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

if __name__=="__main__":
    app=QApplication(sys.argv)
    cI=transInfo()
    cI.show()
    sys.exit(app.exec())