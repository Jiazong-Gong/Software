from UI.导游信息 import *
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from AddGuide import *
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox
import pymssql
class guideInfo(QMainWindow,Ui_MainWindowGuide):
    def __init__(self,parent=None):
        super(guideInfo,self).__init__(parent)
        self.setupUi(self)

        self.pushButtonSearch.clicked.connect(self.results)
        self.pushButtonRegister.clicked.connect(self.toRegister)
        self.pushButtonSearchDelete.clicked.connect(self.delete)
        self.setObjectName("GuideInfo")
        self.setStyleSheet(
            "#GuideInfo{border-image:url(pic/2.jpg);}"
            "#pushButtonSearch{border-radius:100px;background-image:url(icon/correct.png);}"
            "#pushButtonRegister{border-radius:100px;background-image:url(icon/add.png);}"
            "#pushButtonSearch:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonRegister:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonSearchDelete:hover{border-radius:100px;background-image:url(icon/hover.png);}"
            "#pushButtonSearchDelete{border-radius:100px;background-image:url(icon/delete.png);}"
        )
    def results(self):
        guideName = self.lineEditName.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "Travel_Agency"
        conn1 = pymssql.connect(server, user, password, database)
        guide_info_search = conn1.cursor()
        guide_info_search.execute("select * from guide where g_name=%s", guideName)
        rows = guide_info_search.fetchall()
        row = guide_info_search.rowcount  # 取得记录个数，用于设置表格的行数
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
    def toRegister(self):
        self.rr=guideAdd()
        self.rr.show()
    def delete(self):
        guideID = self.lineEditNo.text()
        server = "JASONK"
        user = "sa"
        password = "123456"
        database = "Travel_Agency"
        conn11 = pymssql.connect(server, user, password, database)
        guide_info_delete = conn11.cursor()
        guide_info_delete.execute("delete from guide where g_id=%s", guideID)
        QMessageBox.information(self, "   ", "DELETING ACCOMPLISHED！")
        conn11.commit()

if __name__=="__main__":
    app=QApplication(sys.argv)
    cI=guideInfo()
    cI.show()
    sys.exit(app.exec())