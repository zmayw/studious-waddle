#coding=utf-8
from sparseGraph import *
from denseGraph import *

import random
def test(g1, N, M):
    for i in range(M):
        a = random.randint(0, N-1)
        b = random.randint(0, N-1)

        g1.addEdge(a, b)

    for v in range(N):
        print ("v:", v),
        adj = SparseGraph.adiIterator(g1, v)
        w = adj.begin()
        while(adj.end()==False):
            print('%d' % w),
            w = adj.next()
        print ''
print "SparseGraph"
N = 20
M = 100
g1 = SparseGraph(N, False)
test(g1, N, M)
print "g1.V(),E()",g1.V(),g1.E()

print "DenseGraph"
N = 20
M = 100
g2 = DenseGraph(N, False)
test(g2,N,M)
print "g2.V(),E()",g2.V(),g2.E()
