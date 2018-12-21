#coding=utf-8

from xml.etree.ElementTree import Element,ElementTree
import requests
from xml_pretty import pretty
from threading import Thread

#线程间的通信
#download为IO密集型操作，使用多线程实现
from Queue import Queue

class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        number = "10101" + str(sid).rjust(2, '0') + '00'
        self.url = "http://www.weather.com.cn/data/sk/%s.html" % number
        self.queue = queue

    def download(self, url):
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

    def run(self):
        print "Download",self.sid
        data = self.download(self.url)
        self.queue.put((self.sid, data))

class ConvertThread(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def jsonToXml(self, json, fxml):
        data = json["weatherinfo"]

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

    def run(self):
        while True:
            sid, data = self.queue.get()
            print "Convert", sid
            if sid == -1:
                break
            if data:
                fname = "10101" + str(sid).rjust(2, '0') + '00'+".xml"
                with open(fname, 'wb') as wf:
                    self.jsonToXml(data,wf)

#test
q = Queue()
dThreads = [DownloadThread(i,q) for i in xrange(1,11)]
cThread = ConvertThread(q)
for t in dThreads:
    t.start()
cThread.start()
for t in dThreads:
    t.join()

q.put((-1,None))
print "---end---"