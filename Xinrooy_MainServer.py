__author__ = 'xinrooy'
#-*- coding: utf-8 -*-
'''
代码片段名称：与外部文件和数据库交互
主要功能：
python版本：
代码教学源:
相关参考文章：
创建时间：
使用说明：
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from login_qrc import *
[335]self.Label_LoginFALSE.setVisible(False)#隐藏登录失败提示信息

from PyQt5 import QtCore, QtGui, QtWidgets
from code_qrc import *
'''
import subprocess,sys
import time
import multiprocessing as mp
import sys
from code import *
from login import *
from PyQt5.QtWidgets import QFileDialog,QTableWidgetItem,QHeaderView,QTableWidget,QApplication,QMainWindow,QDialog
from PyQt5.QtCore import *
from PyQt5 import Qt
from PyQt5.QtWidgets import QMessageBox #错误提示窗口
#调用其他文件的通用类
from TY_RW_Files import *
from PyQt5.QtWidgets import *
'''
登录窗体
'''
#【1】以下的类是构建窗体的类
class XM_Windows_P1(QMainWindow):#登录界面的类
    Signal_Login_Error=pyqtSignal()#登录错误的信号
    def __init__(self):
        QMainWindow.__init__(self)
        #实例化登录窗体
        self.main_ui =Ui_LoginForm()
        self.main_ui.setupUi(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)#隐藏窗体边框
        self.main_ui.PushButton_Close.clicked.connect(self.CloseWindows)#点击关闭按键关闭窗体
        self.main_ui.PushButton_Minimize.clicked.connect(self.MinimizeWindows)#点击最小化按键最小化窗体
        self.main_ui.PushButton_Login.clicked.connect(self.Get_LineEdit_Login_data)#点击登录按键获取登录信息
        self.Signal_Login_Error.connect(self.Show_Login_Error)#登录错误信号触发修改界面上错误提示状态
    def CloseWindows(self):#关闭窗口
        self.setWindowFlags(Qt.Qt.WindowCloseButtonHint)
    def MinimizeWindows(self):#最小化窗口
        self.setWindowFlags(Qt.Qt.WindowMinimizeButtonHint)
    def Show_Login_Error(self):#显示登录失败提示信息
        QMessageBox.information(self,"错误","登录信息错误，请重新输入",QMessageBox.Yes)
        print('修改登录提示')
class XM_Windows_P2(QMainWindow):#主页面code的窗体类
    Signal_Login_InitProject=pyqtSignal()#登录成功后初始化项目配置的界面信号
    Signal_Change_comboBoxItem=pyqtSignal(list,str)#修改项目名称下拉框内容
    def __init__(self):
        QDialog.__init__(self)
        #实例化code窗体
        self.child=Ui_MainWindow()
        self.child.setupUi(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)#隐藏窗体边框
        #点击按键关闭和最小化窗体
        self.child.PushButton_close.clicked.connect(self.CloseWindows)#点击关闭按键关闭窗体
    def CloseWindows(self):#关闭窗体
        self.setWindowFlags(Qt.Qt.WindowCloseButtonHint)
    def MinimizeWindows(self):#最小化窗体
        self.setWindowFlags(Qt.Qt.WindowMinimizeButtonHint)
    def ShowWindows(self):#显示窗体
        MainWindow = QtWidgets.QMainWindow()
        self.child.setupUi(MainWindow)
        MainWindow.show()

#【2】以下的类是构建窗体运行的类
class XM_UI_process():
    def __init__(self):
        app=QApplication(sys.argv)
        login_window=XM_Windows_P1()#登录界面的实例化
        code_window=XM_Windows_P2()#主界面的实例化
    def Run_P2(self):#运行启动主页
        app = QtWidgets.QApplication(sys.argv)
        code_window=XM_Windows_P2()
        code_window.show()
        code_window.Signal_Login_InitProject.emit()#显示主界面之后立刻发射信号进行项目信息的初始化
        sys.exit(app.exec_())
if __name__ == '__main__':
    #启动软件界面线程
    Run_UI_process=XM_UI_process()
    UI_process= mp.Process(target=XM_UI_process,name='兴瑞远智能开发系统-登录')
    UI_process.start()