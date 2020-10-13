__author__ = 'Xinrooy'
from Xinrooy_index import *
import sys
import Xinrooy_index
from condb import HY_condb
from website import HY_WebSite
from PyQt5.QtWidgets import QApplication, QMainWindow
class hyText(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(hyText,self).__init__()
        QMainWindow.__init__(self)
        self.miui = Ui_MainWindow()
        self.miui.setupUi(self)
        self.miui.PushButton_Login_13.clicked.connect(self.onClick)#提交糙
        self.miui.PushButton_Login_15.clicked.connect(self.WebAuto)
    def onClick(self):
        Hyserver = self.miui.lineEdit_server_IP_2.text()
        HyUser = self.miui.lineEdit_11.text()
        HyPassWord = self.miui.lineEdit_15.text()
        HyDbName = self.miui.lineEdit_35.text()
        try:
            hy = HY_condb(host = Hyserver, user = HyUser, pwd = HyPassWord, db = HyDbName) #实例化数据库连接类
            hy.GetConnect()#调用链接函数
        except:
            print("链接失败")
    def WebAuto(self):
        Hyserver = self.miui.lineEdit_server_IP_2.text()
        HyUser = self.miui.lineEdit_11.text()
        HyPassWord = self.miui.lineEdit_15.text()
        HyDbName = self.miui.lineEdit_35.text()
        hy = HY_condb(host = Hyserver, user = HyUser, pwd = HyPassWord, db = HyDbName)
        hy.HY_auto()
if __name__ == '__main__':
            app = QApplication(sys.argv)
            hy = hyText()
            hy.showFullScreen()
            hy.show()
            print("启动成功")
            sys.exit(app.exec_())
