# -*- coding:utf-8 -*-
import requests
import os,sys
from xlwt import *
import json
from time import ctime,sleep
import threading
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')


conn = MySQLdb.connect(host='192.168.10.113',port=3306,user='root',passwd='****',db='****',charset='utf8')
cur = conn.cursor()

titles = ["officialLogo","orgId","orgName","src","isAuth","markCount","markType","markTitle","callBgPicture","callBgVideo","markBgPictureType","markBgPictureContent",
          "markBgPicture","phoneMenu","officialPhone","postcode","offcialWebsite","weiboUrl","longitude","latitude","address","className1","className2"]

def sendToRequestsAndRecordResponse(titles, msgNumberFilePath,excelName):
    print "start to do the numberfile %s : %s" % (msgNumberFilePath,ctime())
    numberFile = open(msgNumberFilePath)
    numbers = numberFile.readlines()
    print len(numbers)

    file = Workbook(encoding='utf-8')
    sheet = file.add_sheet(excelName)
    for i in range(len(numbers)):
        url = "http://callmemsg.wostore.cn/kaomi/getPhoneDetail"
        number = numbers[i]
        number = number.replace("\n","")
        print number
        params= {
            "phone_number": number,
            "imei": ""
        }
        Response = requests.post(url,json=params)
        #time.sleep()
        print Response.json()
        if Response.json().has_key ("code"):
            sheet.write(i, 0, number)
            print number
        else:
            #print "R"
            resJson = Response.json()
            resData=[]
            resData.append(number)
            for title in titles:
                if Response.json().has_key(title):
                    resData.append(resJson[title])
                    print title, type(resJson[title])
                else:
                    pass
                    #resData.append('null')
                #print resData
            #for j in range(len(resData)):
                #sheet.write(i,j,resData[j])
            sql = 'insert into table1 (' + ','.join(resData.keys()) + ') values(%s' + ',%s' * (len(resData)-1) + ');'
            print sql
            cur.execute(sql,resData.values())
            conn.commit()
   # file.save("%s.xls" % excelName)


threads=[]
for i in range(1):
    numberfile = "number%s.txt" % i
    excelName = "number%s" % i
    print numberfile
    t = threading.Thread(target=sendToRequestsAndRecordResponse, args=(titles,numberfile,excelName))
    threads.append(t)

if __name__ == '__main__':
    print threading
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    cur.close()
    conn.commit()
    conn.close()
    print "all over %s" % ctime()
