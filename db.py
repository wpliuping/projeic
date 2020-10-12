__author__ = 'Xinrooy'
# -*- coding: utf-8 -*-
from condb import HY_condb
from website import HY_WebSite
from operation_db import HY_find
if __name__ == '__main__':
    HyCon = HY_condb(host="DESKTOP-28K83S0\XINROOY",user="xinrooy",pwd="xinrooy",db="xinrooytest")
    date = HyCon.HY_finddate('select MFR_DATE, MFR_PN, MFR_LOT from dbo.people_one')
    print(date)
