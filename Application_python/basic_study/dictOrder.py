#coding=utf-8

from time import time
from random import randint
from collections import OrderedDict
#模拟一个比赛系统
#使用collections OrderedDict，使字典有序
players = list('ABCDEFGH')
start = time()
d = OrderedDict()
for i in xrange(8):
    raw_input()
    p = players.pop(randint(0,7-i))
    end = time()
    print i + 1, p, end-start
    d[p] = (i+1, end-start)
print ""
print "The Result"
for k in d:
    print k,d[k]