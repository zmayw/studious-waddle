#coding=utf-8
from random import randint

#1.找出序列中出现频次最多的元素
data = [randint(0, 20) for _ in xrange(30)]
res = dict.fromkeys(data,0)
for i in data:
    res[i] += 1
print res

#2.使用collections下的Counter对象
from collections import Counter
res2 = Counter(data)
print res2
print res2.most_common(3)