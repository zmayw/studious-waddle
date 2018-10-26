#coding:utf8

import sys,os

import unittest
import requests
sys.path.append("..")
from diff_dict import *

class MyTestCase(unittest.TestCase):
    #('中国联通','中国移动','中国电信','交通银行','建设银行','招商银行','工商银行','铁路客服','中国南方航空','华夏银行')
    #('10010','10086','10001','95559','95533','95555','95588','12306','95539','95577')
    #'10086','10010','10001','95559','95533','12306','95555','95588','95539','95311','95511','95508','95577'

    def stest_msgOrgData(self):
        url_lt = "http://192.168.1.202:7771/api/v1/msgOrgData"
        url_new = "http://192.168.1.202:8881/api/v1/msgOrgData"
        #msgNumbers = ('10010','10086','10001','95559','95533','95555','95588','12306','95539','95577','1069015978280')
        msgNumbers =('1069015978280',)
        for msgNumber in msgNumbers:
            params = {
                "sysModel":"",
                "channelId":"1006585400006",
                "msgNumberList":[
                {
                    "lastModified":0,
                    "msgNumber":msgNumber
                }
                ]
            }
            response_lt = requests.post(url_lt,json=params)
            response_new = requests.post(url_new,json=params)
            print "请求号码:%s" % msgNumber
            print "-------------请求联通MCS接口结果如下----------------"
            print response_lt.json()
            print "-------------请求合库后联通MCS接口结果如下----------"
            print response_new.json()
            meslist = []
            res = diff_dict(response_lt.json(),response_new.json(),meslist)
            display_meslist(res)

    def  test_msgCardData(self):
        url_lt = "http://192.168.1.202:7771/api/v1/msgCardData"
        url_new = "http://192.168.1.202:8881/api/v1/msgCardData"
        #msgNumbers = ('10010','10086','10001','95559','95533','95555','95588','12306','95539','95577',"10690081695")
        msgNumbers =('10690081695',)
        for msgNumber in msgNumbers:
            params = {
                "sysModel":"",
                "channelId":"1006585400006",
                "msgNumberList":[
                {
                    "lastModified":0,
                    "msgNumber":msgNumber
                }
                ]
            }
            response_lt = requests.post(url_lt,json=params)
            response_new = requests.post(url_new,json=params)
            print "请求号码:%s" % msgNumber
            print "-------------请求联通MCS接口结果如下----------------"
            print response_lt.json()
            print "-------------请求合库后联通MCS接口结果如下----------"
            print response_new.json()
            meslist = []
            res = diff_dict(response_lt.json(),response_new.json(),meslist)
            display_meslist(res)

    def  stest_getJsContent(self):
        url_lt = "http://192.168.1.202:7771/api/v1/getJsContent"
        url_new = "http://192.168.1.202:8881/api/v1/getJsContent"
        #msgNumbers = ('10010','10086','10001','95559','95533','95555','95588','12306','95539','95577')
        params = {
                "sysModel": "",
                "areaNumber": "",
                "channelId": "1006585400006",
                "lastModified": "",
                "phoneManufacturer": "unknown"
        }
        response_lt = requests.post(url_lt,json=params)
        response_new = requests.post(url_new,json=params)
        # print "-------------请求联通MCS接口结果如下----------------"
        print response_lt.json()
        #print "-------------请求合库后联通MCS接口结果如下----------"
        print response_new.json()
        meslist = []
        res = diff_dict(response_lt.json(),response_new.json(),meslist)
        display_meslist(res)

if __name__ == '__main__':
    unittest.main()
