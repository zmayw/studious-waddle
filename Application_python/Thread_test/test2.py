#coding=utf-8
import requests
import xml
import csv
from xml.etree.ElementTree import Element,ElementTree
from xml_pretty import pretty
from StringIO import StringIO
from threading import Thread



def download(url):
    response = requests.get(url)
    if response.ok:
        return StringIO(response.content)

def csvToXml(scsv,fxml):
    reader = csv.reader(scsv)
    print "reader",reader.next().tag ,reader.next()
    headers = reader.next()
    headers = map(lambda h: h.replace(' ', ''), headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag, text in zip(headers,row):
            e = Element(tag)
            e.text = text
            eRow.append(e)

        pretty(root)
        et = ElementTree(root)
        et.write(fxml)

def getJson(url):
    params ={
        "Accept":	"text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection":"keep-alive",
        "Host":"www.weather.com.cn",
        "Upgrade-Insecure-Requests":1,
        "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0"
    }
    response = requests.get(url, headers=params)
    if response.ok:
        return response.json()

def jsonToXml(json, fxml):
    data = json["weatherinfo"]
    print data

    root = Element('Data')
    for row in data:
        eRow = Element('Row')
        root.append(eRow)
        for k, v in data.items():
            e = Element(k)
            e.text = v
            eRow.append(e)

        pretty(root)
        et = ElementTree(root)
        et.write(fxml)

def handle(sid):
    print "Download...(%d)" % sid
    number = "1011101" + str(sid).rjust(2, '0')
    url = "http://www.weather.com.cn/data/sk/%s.html" % number #101110101
    rf = getJson(url)
    if  rf is None:
        return
    print "Convert to xml...(%d)" % sid
    fname = number + '.xml'
    with open(fname, 'wb') as wf:
        jsonToXml(rf, wf)

#if __name__ == '__main__':

    #url = "http://www.weather.com.cn/data/sk/101110101.html"
    # t = Thread(target=handle,args=(1,))
    # t.start()
    # print 'main thread'

from threading import Thread
#1.方法一
# t = Thread(target=handle, args=(1,))
# t.start()
# print 'main thread'

#2。方法二，定义类

class MyThread(Thread):

    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid

    def run(self):
        self.handle(self.sid)


    def handle(self, sid):
        print "Download...(%d)" % sid
        number = "10101" + str(sid).rjust(2, '0') + '00'
        print number
        url = "http://www.weather.com.cn/data/sk/%s.html" % number #101110101
        rf = self.getJson(url)
        if  rf is None:
            return
        print "Convert to xml...(%d)" % sid
        fname = number + '.xml'
        with open(fname, 'wb') as wf:
            jsonToXml(rf, wf)

    def getJson(self,url):
        params = {
        "Accept":	"text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection":"keep-alive",
        "Host":"www.weather.com.cn",
        "Upgrade-Insecure-Requests":1,
        "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0"
        }
        response = requests.get(url, headers=params)
        if response.ok:
            return response.json()
#test
threads = []
for i in xrange(1, 11):
    t = MyThread(i)
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print 'main thread'