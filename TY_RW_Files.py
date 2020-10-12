__author__ = 'xinrooy-13'
#-*- coding: utf-8 -*-
'''
代码片段名称：与外部文件和数据库交互
主要功能：
python版本：
代码教学源:
相关参考文章：
创建时间：
使用说明：
configparser:
pip install configparser
'''
import subprocess,sys
import configparser
import pandas as pd

'''
TY_RW_IniFiles类主要功能是读写ini文件类型的配置文件。
R_IniFiles函数是读取文件FilesURL：文件路径,Read_Place读取位置,Read_Content
'''
class TY_RW_IniFiles(object):
    def R_IniFiles(self,FilesURL,Read_Place,Read_variable):#读取配置文件
        #FilesURL：需要读取文件的路径；
        #Read_place：读取位置参数，在配置文件中带有[]的参数；
        #Read_Content：读取的内容
        try:
            config = configparser.ConfigParser()#实例化configparser中的ConfigParser类
            config.read(FilesURL)#调用读取文件的函数
            if Read_Place!='null':#判断读取位置是否为空，为空时
                Read_content=config.get(Read_Place,Read_variable)#使用获取变量找到需要获取的变量，将获取的内容返回
                #print(Read_content)
                return Read_content#返回读取的内容
            else:
                print('Read_Place参数不能为空，否则无法读取内容')#如果读取位置为空则提示
        except:
            print("无法打开Ini文件")
    def W_IniFiles(self,FilesURL,Save_place,Save_variable,Save_content):#将内容存入配置文件
        #FilesURL：文件路径法
        #Save_place：存储位置
        #Save_variable：存储变量
        #Save_content：存储内容
        try:
            config = configparser.ConfigParser()#实例化configparser中的ConfigParser类
            config.read(FilesURL)#调用读取文件的函数
            #判断是存还是取
            if Save_place!='null':#判断存储位置是否为空
                config.set(Save_place,Save_variable,Save_content)#将存储内容存入文件
                with open(FilesURL,'w') as configfile:
                    config.write(configfile)
                print("【OK】完成配置文件的修改")
                Check_Read= config.get(Save_place,Save_variable)#获取存入的内容
                if Check_Read==Save_content:#确认存入的内容是否为目标存入内容
                    print("【OK】保存修改配置文件成功")
                    If_save=True#保存完成为1
                    return If_save
                else:
                    print("【Error】配置文件存储错误")
                    If_save=False#保存未完成为0
                    return If_save
        except:
            print("无法打开Ini文件")
'''
TY_RW_Excel：读写Excel的内容
'''
# class TY_RW_Excel:
#     def R_Excel_SheetName(self,FilesURL):#获取整个表格的Sheet页的名字
#         #FilesURL：读取的Excel文件的路径
#         excel_reader=pd.ExcelFile(FilesURL)  # 指定文件
#         SheetName= excel_reader.sheet_names
#         return SheetName#返回的是Sheet的名字list
#     def R_Excel_OneSheet(self,FilesURL,SheetName,DataFrame_Header,DataFrame_Index):#读取Excel的某个Sheet页
#         #FilesURL：读取的Excel文件的路径
#         #SheetName：需要读取的Sheet的名字
#         #DataFrame_Header：读取的表格以哪一行作为表头
#         #DataFrame_Index：以那一列作为读取后的表的索引[0,1](以第一列)
#         try:
#             InSheetContent=pd.read_excel(FilesURL,header=DataFrame_Header,sheet_name=SheetName,index_col=DataFrame_Index)#encoding='utf-8',
#             InSheetContent= pd.DataFrame(InSheetContent)
#             return InSheetContent#返回DataFrame的整个表格的数据
#         except:
#             print("读取excel文件出错")
#             return '读取excel文件出错'
#     def W_Excel_OneSheet(self,FilesURL,SheetName,DataFrame_Content,Write_Model):#将一个表格数据写入一个表格的Sheet页中
#         #FilesURL：写入的Excel文件的路径
#         #SheetName：写入的Sheet页名字
#         #DataFrame_Content：写入的表格内容
#         #Write_Model:写入表格的时候是插入还是覆盖原有表格，有'append'和'replace'两种
#         try:
#             if Write_Model=='append':
#                 excel_writer = pd.ExcelWriter(FilesURL,mode='a',engine='openpyxl')  # 定义writer，选择文件（文件可以不存在）
#             else:
#                 excel_writer = pd.ExcelWriter(FilesURL)  # 定义writer，选择文件（文件可以不存在）
#             df = pd.DataFrame(DataFrame_Content)
#             df.to_excel(excel_writer, sheet_name=SheetName, index=False)  # 写入指定表单
#             excel_writer.save()  # 储存文件
#             excel_writer.close()  # 关闭writer
#             If_write=True
#             return If_write#返回是否完成写入的标注
#         except:
#             print("写入excel文件出错")
#             return '写入excel文件出错'
class TY_Open_Files(object):#打开文件
    def Open_Files(self,FilesURL):#打开指定文件
        try:
            open(FilesURL, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
            print('打开文件成功')
            return True
        except:
            print('打开文件失败')
            return False
# class TY_OpenExe():
#     def Open_Exe(self,Path):
#         try:
#             subprocess.Popen(Path)
#         except:
#             print('打开可执行性文件失败，请检查exe文件是否存在')


# URL=r'config.ini'
# Run_TY_Open_Files=TY_Open_Files()
# RunOpenFile = TY_RW_IniFiles()
# Run_TY_Open_Files.Open_Files(URL)
# RunOpenFile.R_IniFiles(URL,"Postgre","port")
# print(RunOpenFile.R_IniFiles(URL,"Postgre","port"))
'''

URL='F:\Py_Project\OdooCode\TY_Package\sheji.xlsx'
Run_TY_RW_Excel=TY_RW_Excel()
Data=Run_TY_RW_Excel.R_Excel_SheetName(URL)
Run_TY_RW_Excel.W_Excel_OneSheet(URL,'Sheet2',Data,'replace')
Run_TY_RW_Excel.W_Excel_OneSheet(URL,'Sheet2',Data,'append')'''
'''

读取Excel测试代码
URL='F:\Py_Project\OdooCode\TY_Package\sheji.xlsx'
Run_TY_RW_Excel=TY_RW_Excel()
print(Run_TY_RW_Excel.R_Excel_OneSheet(URL,0,0,[0,1]))'''

'''
#读取Ini文件的测试代码
URL='F:/Py_Project/XinrooyCodeCreater/config.ini'
Run_TY_RW_IniFiles=TY_RW_IniFiles()
print(Run_TY_RW_IniFiles.R_IniFiles(URL,'Postgre','host'))'''
