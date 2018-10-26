# -*- coding:utf-8 -*-

import requests, MySQLdb
import json
import sys
import codecs
from xlwt import *
import xlrd
from xlutils.copy import copy
reload(sys)
import re
sys.setdefaultencoding('utf-8')

#data = xlrd.open_workbook("query_result.xls")
#table = data.sheets()[0]
#wb = copy(data)
#ws = wb.get_sheet(0)
#rowsCount = table.nrows
numbersFile = open("query_result2.txt")
linesContent = numbersFile.readlines()

file = Workbook(encoding='utf-8')
sheet = file.add_sheet("msgNumbers")


conn = MySQLdb.connect(host="192.168.10.113", user="root", passwd="****", db="***",charset="utf8")
cursor = conn.cursor()
for index in range(len(linesContent)):
    print index
    line = linesContent[index].split(",")
    print linesContent[index]
    print line
    msgNum = line[0]
    orgId = line[2].replace('"',"")
    orgName = line[4]
    print msgNum
    print orgId
    sql_msgNum = "select id from org_msg_num where org_id='%s' and msg_num='%s';" % (orgId,msgNum)
    print sql_msgNum
    cursor.execute(sql_msgNum)
    results_msgNum = cursor.fetchall()
    sheet.write(index,0,msgNum)
    sheet.write(index,1,orgId)
    sheet.write(index,2,orgName)
    if len(results_msgNum)==0:
        sheet.write(index,3,"numNotExist")
    else:
       msgNumId = results_msgNum[0][0]
       sql_media = "select img_url from org_media where org_id='%s' and content_type=4 and (channel_id='1006585400001' or channel_id='dfee55ef6e5d4836959c01519f6624e1') and `remove`=0;" % orgId
       sql_menu = "select audit_status,channel_id from org_menu where org_id='%s' and parent_id is NULL and menu_type='sms' " \
                  "and audit_status in ('online','offline') and (channel_id='1006585400001' or channel_id='dfee55ef6e5d4836959c01519f6624e1') and `remove`=0;" % orgId
       sql_card = "select id,title,card_content,audit_status from msg_card where msg_number_id='%s' " \
                  "and audit_status in ('online') and (channel_id='1006585400001' or channel_id='dfee55ef6e5d4836959c01519f6624e1') and `remove`=0;" % msgNumId
       #返回菜单状态，记录在EXCEL，是否有菜单，菜单状态
       cursor.execute(sql_media)
       results_media = cursor.fetchall()
       cursor.execute(sql_menu)
       results_menu = cursor.fetchall()
       cursor.execute(sql_card)
       results_card = cursor.fetchall()
      # print str(results_card).decode('unicode')
       if len(results_media)!=0:
            sheet.write(index,4,"http://file.cctocloud.com/"+str(results_media[0][0]).decode("unicode_escape"))
       sheet.write(index,5,str(results_menu).decode("unicode_escape"))
       sheet.write(index,6,str(results_card).decode("unicode_escape"))

file.save("msgNumbers.xls")
cursor.close()
conn.close()