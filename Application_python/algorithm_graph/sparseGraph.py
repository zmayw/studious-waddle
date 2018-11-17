#coding=utf-8

class SparseGraph:

    def __init__(self,n,directed):
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

    def addEdge(self,v,w):
        self.outOfRang(v, self.n)
        self.outOfRang(w, self.n)
        self.g[v].append(w)
        if(v != w and self.directed==False):
            self.g[w].append(v)
        self.m += 1

    def hasEdge(self, v, w):
        self.outOfRang(v, self.n)
        self.outOfRang(w, self.n)
        len = len(self.g(v))
        for i in range(len):
            if self.g[v][i] == w:
                return True
        return False

        #[begin_index,len)
    def outOfRang(self,x,len,begin_index=0):
         if ( x < begin_index or x>= len):
            raise "The node is out of range(0-%d)" % len


    #显示图的信息
    def show(self):
        for i in range(self.n):
            m = len(self.g[i])
            for j in range(m):
                print(self.g[i][j]),
            print ""

    class adiIterator(object):
        '''相邻节点迭代器'''
        def __init__(self,graph,v):
            self.G = graph #需要遍历的图
            self.v = v  #遍历V节点相邻的边
            self.index = 0 #遍历的索引

        def next(self):
            self.index += 1
            if(self.index < len(self.G.g[self.v])):
                return self.G.g[self.v][self.index]

        def begin(self):
            if(len(self.G.g[self.v]) > 0):
                return self.G.g[self.v][0]
            return -1

        def end(self):
            return self.index >= len(self.G.g[self.v])
