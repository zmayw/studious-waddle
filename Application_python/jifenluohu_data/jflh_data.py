#coding=utf-8

import urllib
import urllib2
import os,re
import requests
from bs4 import BeautifulSoup
from xlwt import *
import time

url_referer = "http://www.bjrbj.gov.cn/integralpublic/settleperson/settlePersonTable/"
params = {"Host": "www.bjrbj.gov.cn", "Referer": url_referer,"X-Requested-With":"XMLHttpRequest"}
#page = urllib2.urlopen(url)

def writeDataToExcel(sheet, data, begin_row):
    colCount = len(data[0])
    for rowNum in range(len(data)):
        for colNum in range(colCount):
            value = data[rowNum][colNum]
            sheet.write(rowNum+begin_row, colNum, value)

file = Workbook(encoding='utf-8')
sheet = file.add_sheet("jflh")
data = []
for i in range(6019/100+1):
    print "page number %s" % i
    url = "http://www.bjrbj.gov.cn/integralpublic/settlePerson/settlePersonJson?sort=pxid&order=asc&" \
          "limit=100&offset=%d&name=&rows=100&page=%d&_=%s" % (i*100,i*100,time.time()*100)
    print url
    response = requests.get(url, params=params)
    res = response.json()
    rows = res["rows"]
    rows_data = []
    headers = ["pxid","name", "score", "unit", "csrq"]
    for row in rows:
        row_data = []
        for item in headers:
            row_data.append(row[item])
        rows_data.append(row_data)
    data.append(rows_data)
    writeDataToExcel(sheet, rows_data, i*100)
file.save("jflu.xls")
print "__end__"




