#coding=utf-8

#线程间的事件通知，可以使用标准库中Threading.Event
#1.等待事件一端庙用wait,等待事件
#2.通知事件一端调用set，通知事件
import tarfile
import os
from threading import Thread, Event
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

    def __init__(self, queue, cEvent, tEvent):
        Thread.__init__(self)
        self.queue = queue
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.count = 0

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
        count = 0
        while True:
            sid, data = self.queue.get()
            print "Convert", sid
            if sid == -1:
                self.cEvent.set()
                self.tEvent.wait()
                break
            if data:
                fname = "10101" + str(sid).rjust(2, '0') + '00'+".xml"
                with open(fname, 'wb') as wf:
                    self.jsonToXml(data,wf)
                count += 1
                if count == 5:
                    self.cEvent.set()
                    self.tEvent.wait()
                    self.tEvent.clear()
                    count = 0


class TarThread(Thread):
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.setDaemon(True)

    def tarXML(self):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname,'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)

        tf.close()

        if not tf.members:
            os.remove(tfname)

    def run(self):
        while True:
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()

            self.tEvent.set()


#test
if __name__ == '__main__':
    q = Queue()
    dThreads = [DownloadThread(i,q) for i in xrange(1,11)]

    cEvent = Event()
    tEvent = Event()
    cThread = ConvertThread(q, cEvent, tEvent)
    tThread = TarThread(cEvent, tEvent)
    tThread.start()

    for t in dThreads:
        t.start()

    cThread.start()

    for t in dThreads:
        t.join()
    q.put((-1,None))
    print 'main thread'


# def tarXML(tfname):
#     tf = tarfile.open(tfname,'w:gz')
#     for fname in os.listdir('.'):
#         if fname.endswith('.xml'):
#             tf.add(fname)
#             os.remove(fname)
#     tf.close()
#
#     if not tf.members:
#         os.remove(tfname)
#tarXML('test.tgz')

# def f(e):
#     print "f 0"
#     e.wait()
#     print "f 1"
#
# e = Event()
# t = Thread(target=f, args=(e,))
# t.start()
# e.set()
# e.clear()
