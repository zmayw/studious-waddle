#encoding:UTF-8

import requests, MySQLdb
import json
import sys,os
import codecs
import re
import xlrd
from xlutils.copy import copy
reload(sys)
sys.setdefaultencoding('utf8')


conn = MySQLdb.connect(host="192.168.x.x", user="*****", passwd="*****", db="*****",charset="utf8")

cursor = conn.cursor()
db_cx = "***"
db_dx = "***"
db_hk = "***"
db_list = [db_cx,db_dx,db_hk]

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,"dbDataCount.xls")
print filename
data = xlrd.open_workbook(filename)
table = data.sheets()[0]
wb = copy(data)
ws = wb.get_sheet(0)
rowsCount = table.nrows

for index in range(rowsCount):
    if index<2: #有效数据从哪行开始，下标从0计
        continue
    sum = 0
    for col in range(3):
        db_table = table.row_values(index)[col+2] #取EXCEL中对应的表名，如超信为第2列、电信为第3列、合库为第4列；列下标从0开始
        db_table = db_table.strip()
        print db_table
        if db_table == "":
            count = 0
        else:
            sql = "select count(*) from `%s`.`%s`;" % (db_list[col],db_table)
            cursor.execute(sql)
            results = cursor.fetchall()
            count = results[0][0]
        if col != 2:
            sum = sum + int(count)
        ws.write(index,col+2+3,count) #取EXCEL中对应库的数据量，如超信为第2+3列、电信为第3+3列、合库为第4+3列；列下标从0开始
    ws.write(index,8,sum) #记录超信、电信表中数量之和
wb.save(filename)

cursor.close()
conn.close()

print "--end--"















