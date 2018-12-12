#coding=utf-8

from random import randint
from timeit import timeit
#如何在列表、字典、集合中根据条件筛选数据
#使用列表解析比使用普通方法的速度几乎可以快1倍。因此推荐使用列表解析。

data = [5,6,-1,2,4,-3,9,8,0,12,-7]
#data = [randint(-10,10) for _ in xrange(10)]

#1.通用处理方法，迭代
def func():
    res = []
    for x in data:
        if x >= 0:
            res.append(x)
    print res


#2.函数式编程
res = filter(lambda x : x >= 0, data)
print res

#3.列表解析
res = [x for x in data if x >= 0]
print res
print timeit('func()','from __main__ import func',number=1)
print timeit('filter(lambda x : x >= 0, [5,6,-1,2,4,-3,9,8,0,12,-7])',number=1)
print timeit('[x for x in [5,6,-1,2,4,-3,9,8,0,12,-7] if x >= 0]',number=1)

