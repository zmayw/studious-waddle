#conding=utf-8
from unionFind1 import *
from unionFind2 import *
from unionFind21 import *
from unionFind3 import *
from unionFind_rank import *
from unionFind_pathCompress import *
import random
import time

def testUF(n,uf):
    startT = time.time()
    for i in range(n):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        uf.unionElements(a,b)

    for i in range(n):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        uf.isConnected(a,b)

    endT = time.time()
    print "time is ", endT-startT

n = 100000
# uf1 = UionFind1(n)
# testUF(n,uf1)
# print "...after optimize 2...."
# uf2 = UnionFind_optimized2(n)
# testUF(n,uf2)
# print "...after optimize 21...."
# uf21 = UnionFind_optimized21(n)
# testUF(n,uf21)

print "...after optimize 3...."
uf3 = UnionFind_optimized3(n)
testUF(n,uf3)

# print "...after optimize rank...."
# uf4 = UnionFind_rank(n)
# testUF(n,uf4)

print "...after optimize pathCompress...."
uf5 = UnionFind_pathCompress(n)
testUF(n,uf5)

# time is  14.7990000248
# ...after optimize....
# time is  2.60899996758

# time is  14.864000082
# ...after optimize....
# time is  0.161000013351