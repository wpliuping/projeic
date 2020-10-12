__author__ = 'Xinrooy'
# -*- coding: utf-8 -*-
from selenium.webdriver import Chrome
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from operation_db import HY_find
from condb import *
name='11101965'
passwd='1'
class HY_WebSite(HY_find):
    def HY_auto(self):
        HY_find1 = HY_condb()
        data = HY_find1.HY_finddate('select MFR_DATE, MFR_PN, MFR_LOT from dbo.people_one')
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
        sleep(100)
        driver.quit()