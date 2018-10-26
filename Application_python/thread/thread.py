#coding=utf-8
import csv
import requests
from xml.etree.ElementTree import Element,ElementTree
from StringIO import StringIO
from xml_pretty import pretty
from threading import Thread
#from collections import deque
from Queue import Queue

class DownloadThread(Thread):
    def __init__(self,sid,queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = "http://table.finance.yahoo.com/table.csv?s=%s.sz"
        self.url %= str(sid).rjust(6,'0')
        self.queue = queue

    def download(self,url):
        response = requests.get(url,timeout=3)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        print "Download ",self.sid
        data = self.download(self.url)
        self.queue.put((self.sid,data))


class ConvertThread(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue = queue

    def csvToXml(self,scsv,fxml):
        reader = csv.reader(scsv)
        headers = reader.next()
        headers = map(lambda h: h.replace(' ',''),headers)

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag,text in zip(headers,row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
        pretty(root)
        et = ElementTree(root)
        et.write(fxml)

    def run(self):
        while True:
            sid,data = self.queue.get()
            print "Convert ",sid
            if sid == -1:
                break
            if data:
                fname = str(sid).rjust(6, '0')+'.xml'
                with open(fname, 'wb') as wf:
                    self.csvToXml(data,wf)



q = Queue()
dThreads = [DownloadThread(i,q) for i in xrange(1,11)]
cThread = ConvertThread(q)
for t in dThreads:
    t.start()
cThread.start()
for t in dThreads:
    t.join()

q.put((-1,None))






