#coding=utf-8
from random import randint, sample
#随机取样
#sample('abcdefg',randint(3,6))
s1 = {x:randint(1,4) for x in sample('abcdeg',randint(3,6))}
s2 = {x:randint(1,4) for x in sample('abcdeg',randint(3,6))}
s3 = {x:randint(1,4) for x in sample('abcdeg',randint(3,6))}
#求s1,s2,s3的公共键

#1.普通迭代方法
res = []
for k in s1:
    if (k in s2) and (k in s3):
        res.append(k)
print res

#2.使用集合的方法，dict.viewkeys()

res = s1.viewkeys() & s2.viewkeys() & s3.viewkeys()
print res

#3.map reduce方法
#map(dict.viewkeys,[s1,s2,s3])
#使用前一个结果a,与当前元素，进行与操作
print reduce(lambda a, b: a & b,map(dict.viewkeys,[s1,s2,s3]))