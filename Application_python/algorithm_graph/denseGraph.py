#coding=utf-8

class DenseGraph:

    def __init__(self,n,directed):
        self.n = n
        self.m = 0
        self.directed = directed
        self.g = []
        for i in range(n):
            lines = []
            for j in range(n):
                lines.append(False)
            self.g.append(lines)

    def V(self):
        return self.n

    def E(self):
        return self.m

    def hasEdge(self,v,w):
        self.outOfRang(v,self.n)
        self.outOfRang(w,self.n)
        if self.directed:
            return self.g[v][w]
        else:
            return (self.g[v][w] and self.g[w][v])

    def addEdge(self, v, w):
        self.outOfRang(v, self.n)
        self.outOfRang(w, self.n)

        if self.hasEdge(v,w):
            return

        self.g[v][w] = True
        if self.directed==False:
            self.g[w][v] = True
        self.m += 1



    #[begin_index,len)
    def outOfRang(self,x,len,begin_index=0):
         if ( x < begin_index or x>= len):
            raise "The node is out of range(0-%d)" % len

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                print '%d' % self.g[i][j],
            print ""


    class adjIterator(object):

        def __info__(self,graph,v):
            self.v = v
            self.index = -1
            self.G = graph

        def begin(self):
            index = -1
            return self.next()

        def next(self):
            self.index += 1
            while(self.index < self.G.V()):
                if(self.G.g[self.v][self.index]):
                    return self.index
                return -1
        def end(self):
            return self.index >= self.G.V()




