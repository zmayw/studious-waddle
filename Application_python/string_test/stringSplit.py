#coding=utf-8

#如何拆分含有多种分陋符的字符串
s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

#1.str.split
def mySplit(str,distinctStr):
    res = [str]
    for d in distinctStr:
        t = []
        map(lambda x: t.extend(x.split(d)),res)
        res = t
    return [x for x in res if x]

def mySplit2(str, distinctStr):
    res = [str]
    for s in distinctStr:
        t = []
        for x in res:
            t.extend(x.split(s))
        res = t
    return [x for x in res if x] #过滤掉空字符串

sd = ";|,\t"
res = mySplit2(s, sd)
print res

#2.re.split
import re

print re.split(r'[,;\t|]+',s)