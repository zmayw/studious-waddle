#coding=utf-8
#import csv
import requests
# import ssl
# # from xml.etree.ElementTree import Element,ElementTree
# # from StringIO import StringIO
# # #from xml_pretty import pretty
# # from threading import Thread
# # #from collections import deque
# # from Queue import Queue
# import urllib3.contrib.pyopenssl
# # import certifi
#
# urllib3.contrib.pyopenssl.inject_into_urllib3()
#
#
# #url = "https://xueqiu.com/stock/forchart/stocklist.json?symbol=SZ399006&period=1d&_=1544863718388"
# #url = "https://xueqiu.com/hq#exchange=CN&plate=1_1_5&firstName=1&secondName=1_1&type=cyb"
# params = {"Accept": "application/json, text/javascript,'*/*; q=0.9,*/*,q=0.8",
#           "Accept-Encoding": "gzip,deflate,br",
#           "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#           "cache-control":"no-cache",
#           "Connection":"keep-alive",
#           "Host": "xueqiu.com",
#           "Referer": "https://xueqiu.com/hq",
#           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
#           "X-Requested-With": "XMLHttpRequest"
# }
# url = "https://xueqiu.com/hq"
#
# # http = urllib3.PoolManager(cert_reqs = 'CERT_REQUIRED',ca_certs="D:\\mayw doc\\SSL\\1215.cer")
# # # #certifi.where()
# # res = http.request('GET',url)
# # print res.status
#
# response = requests.get(url, verify=False)  # "D:\\mayw doc\\SSL\\1215.cer" #DigiNotarRootCA #"D:/mayw doc/SSL/DigiNotarPKIoverheidCAOrganisatie-G2.crt"
# print response