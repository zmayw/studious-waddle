#coding=utf-8
from edge import *
class SparseGraph:

    def __init__(self, n, directed):
        self.n = n
        self.m = 0
        self.directed = directed
        self.g = []
        for i in range(n):
            self.g.append([])

    def V(self):
        return self.n

    def E(self):
        return self.m

    def addEdge(self, v, w, weight):
        self.outOfRang(v, self.n)
        self.outOfRang(w, self.n)
        edge = Edge(v, w, weight)
        self.g[v].append(edge)
        if( v != w and self.directed == False ):
            edge = Edge(w, v, weight)
            self.g[w].append(edge)
        self.m += 1

    def hasEdge(self, v, w, weight):
        self.outOfRang(v, self.n)
        self.outOfRang(w, self.n)
        len = len(self.g(v))
        for i in range(len):
            edge = self.g[v][i]
            if(edge.v() == v and edge.w() == w and edge.weight == weight):
                return True
        return False

        #[begin_index,len)
    def outOfRang(self, x, len, begin_index=0):
         if(x < begin_index or x >= len):
            raise "The node is out of range(0-%d)" % len


    #显示图的信息
    def show(self):
        for i in range(self.n):
            m = len(self.g[i])
            print "vertex:%d: " % i,
            for j in range(m):
                edge = self.g[i][j]
                print("( to:%s,wt:%f)" % (edge.w(), edge.weight())),
            print ""

    class adjIterator(object):
        '''相邻节点迭代器'''
        def __init__(self,graph,v):
            self.G = graph #需要遍历的图
            self.v = v  #遍历V节点相邻的边
            self.index = 0 #遍历的索引

        def next(self):
            self.index += 1
            if(self.index < len(self.G.g[self.v])):
                return self.G.g[self.v][self.index]
            return None

        def begin(self):
            if(len(self.G.g[self.v]) > 0):
                return self.G.g[self.v][0]
            return None

        def end(self):
            return self.index >= len(self.G.g[self.v])
