__author__ = 'Xinrooy'
# -*- coding: utf-8 -*-

import pymssql
from selenium.webdriver import Chrome
from selenium import webdriver
import time
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
name='11101965'
passwd='1'
class HY_condb:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
    def GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor() #创建一个游标对象,python里的sql语句都要通过cursor来执行
        print("数据库连接成功")
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur
    def HY_finddate(self,sql):
        cursor = self.GetConnect()
        cursor.execute(sql)   #执行sql语句
        dbdate = cursor.fetchone() #读取查询结果
        self.conn.close()
        return dbdate
    def HY_auto(self):
        # HY_find1 = HY_condb()
        data = self.HY_finddate('select MFR_DATE, MFR_PN, MFR_LOT from dbo.people_one')
        MFR_DATE = data[0]
        MFR_PN = data[1]
        MFR_LOT = data[2]
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.implicitly_wait(10)#智能等待
        url = 'http://218.32.15.49:6688/YOUNG_LABEL/Menu/login_user.jsp'
        driver.get(url)
        driver.find_element_by_name('loginId').send_keys(name)
        driver.find_element_by_name('password').send_keys(passwd)
        driver.find_element_by_class_name('button02').click()
        driver.switch_to.frame('menu')
        driver.find_element_by_link_text("open all").click()
        driver.find_element_by_link_text("101 Material Label Printing").click()
        driver.switch_to.default_content()
        driver.switch_to.frame('main')
        driver.find_element_by_name('MFR_DATE').send_keys(MFR_DATE)
        driver.find_element_by_name('MFR_PN').send_keys(MFR_PN)
        driver.find_element_by_name('MFR_LOT').send_keys(MFR_LOT)
        time.sleep(2)
        driver.quit()
    # def HyCondb(self, DbServer, DbUser,DbPassword, DbName):
    #     try:
    #         connect = pymssql.connect(DbServer, DbUser, DbPassword, DbName)
    #         if connect:
    #              print("数据库连接成功")
    #     except:
    #         print("数据库链接失败")

        # try:
        #     URL=r'config.ini'
        #     Run_TY_Open_Files=TY_Open_Files()
        #     RunOpenFile = TY_RW_IniFiles()
        #     Run_TY_Open_Files.Open_Files(URL)
        #     Hyserver = RunOpenFile.R_IniFiles(URL,"Postgre","host")
        #     print(Hyserver)
        #     # HyPort = RunOpenFile.R_IniFiles(URL,"Postgre","port")
        #     HyUser = RunOpenFile.R_IniFiles(URL,"Postgre","user")
        #     print(HyUser)
        #     HyPassWord = RunOpenFile.R_IniFiles(URL,"Postgre","password")
        #     print(HyPassWord)
        #     HyDbName = RunOpenFile.R_IniFiles(URL,"Postgre","database")
        #     print(HyDbName)
        #     connect = pymssql.connect(Hyserver, HyUser, HyPassWord, HyDbName )
        #     print("连接成功")
        # except:
        #     print("链接失败")
    # connect = pymssql.connect('DESKTOP-28K83S0\XINROOY', 'xinrooy', 'xinrooy', 'xinrooytest')  #建立连接
    # if connect:
    #     print("连接成功!")
