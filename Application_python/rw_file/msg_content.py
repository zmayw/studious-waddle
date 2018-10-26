# -*- coding:utf-8 -*-

import requests, MySQLdb
import json
import sys
import codecs
from xlwt import *
reload(sys)
import re
sys.setdefaultencoding('utf-8')

def writeDataToExcel(sheet,data,rowindex):
    for i in range(len(data)):
         sheet.write(rowindex, i, data[i])

keywordsfile = open("keyWords.txt")
linesContent = keywordsfile.readlines()
keywords = {}
for line in linesContent:
    lineArray = line.split("	")
    keywords[lineArray[0]] = lineArray[1].replace("\n", '')

conn = MySQLdb.connect(host="xxx.xxx.xx.xxx", user="test", passwd="****", db="message_content",charset="utf8")
cursor = conn.cursor()
ownerIds = {}
mixIds = {}
codes = keywords.keys()
codes.sort(reverse=True)
print codes
for k in codes:
    sql = "select id,msgContent,msgNumber,receive_time " \
          "from t_msgcontent where msgContent like '%"+keywords[k]+"%' and (id<=100000) group by msgContent;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        msgContent = row[1]
        msgNumber = row[2]
        receive_time = row[3].strftime("%Y-%m-%d %H:%M:%S")
        if ownerIds.has_key(id):
            if mixIds.has_key(id):
                mixIds[id][3].append(k)
                mixIds[id][4].append(keywords[k])
            else:
                mixIds[id] = [ownerIds[id][0],ownerIds[id][1], ownerIds[id][2], [ownerIds[id][3]],[ownerIds[id][4]]]
                mixIds[id][3].append(k)
                mixIds[id][4].append(keywords[k])
            del ownerIds[id]
        else:
            ownerIds[id] = [msgContent, msgNumber, receive_time, k, keywords[k]]
        #newrow = [k, v, id, msgContent, msgNumber, receive_time]
        #writeDataToExcel(sheet,newrow,index)
        #index = index + 1
#file.save("1.xls")
print len(ownerIds)
print len(mixIds)
file = Workbook(encoding='utf-8')
sheet = file.add_sheet("mixIds")
#mixIds.keys().sort()
for i in range(len(mixIds.keys())):
    id = mixIds.keys()[i]
    sheet.write(i,0,id)
    for j in range(len(mixIds[id])):
        value = mixIds[id][j]
        if type(value)==list and len(value)>1:
            value = ','.join(value)
        sheet.write(i,j+1,value)

sheet = file.add_sheet("ownerIds")
for i in range(len(ownerIds.keys())):
    id = ownerIds.keys()[i]
    sheet.write(i,0,id)
    for j in range(len(ownerIds[id])):
        value =  ownerIds[id][j]
        sheet.write(i,j+1,value)

file.save("msgContent.xls")
cursor.close()
conn.close()