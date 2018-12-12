#coding=utf-8
from random import randint
data = {x: randint(60,100) for x in xrange(1,21)}
print data

#1.列表解析
res = { k : v for k, v in data.iteritems() if v > 90}
print res

data2 = data = [5,6,-1,2,4,-3,9,8,0,12,-7]
s = set(data)
res = {x for x in s if x % 3 == 0}
print res

