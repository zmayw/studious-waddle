#coding=utf-8
from sparseGraph import SparseGraph
from edge import Edge

class BellmanFord:

    def __init__(self,graph,s):
        self.__G = graph
        self.__s = s
        self.__from = []
        self.__distTo = []
        self.__hasNegativeCycle = False
        n = self.__G.V()
        for i in range(n):
            self.__from.append(None)
            self.__distTo.append(None)
        self.__distTo[s] = 0
        self.__from[s] = Edge(s, s, 0)

        # Bellman-Ford的过程
        #进行V-1次循环,每一次循环求出从起点到其余所有点，最多使用i步可到达的最短距离
        for i in range(1, n):
            #每次循环中对所有的边进行一遍松驰操作
            #遍历所有边的方式是1.先遍历所有的顶点，2.然后遍历和所有顶点相邻的所有边
            for v in range(n):
                adj = self.__G.adjIterator(self.__G, v)
                edge = adj.begin()
                while adj.end() == False:
                    w = edge.other(v)
                    weight = self.__distTo[v] + edge.weight()
                    #对于每一个边首先判断e.v()是否可达
                    #之后看如果e.w()以前没有到达过，显示可以更新distTo[w]
                    #或者e.w()以前到达过，但是通过edge我们可以获得一个更短信距离，即可以进行一次松驰操作
                    if (self.__from[v]) or (self.__from[w]==None or self.__distTo[w] < weight):
                        self.__distTo[w] = weight
                        self.__from[w] = edge
                    edge = adj.next()

        self.__hasNegativeCycle = self.detectNegativeCycle()

    def detectNegativeCycle(self):
        for i in range(self.__G.V()):
            adj = self.__G.adjIterator(self.__G, i)
            edge = adj.begin()
            while adj.end() == False:
                weight = self.__distTo[edge.v()] + edge.weight()
                if (self.__from[edge.v()]  and weight < self.__distTo[edge.w()]):
                    return True
                edge = adj.next()

        return False

    def negativeCycle(self):
        return self.__hasNegativeCycle

    def shortestPathTo(self, w):
        if(w < 0 or w > self.__G.V()):
            raise "Out of index"
        if self.__hasNegativeCycle == False:
            raise "Graph has negative Cycle!"
        if self.hasPathTo(w)==False:
            raise "Not exist path to this vertex"
        return self.__distTo[w]

    def hasPathTo(self,w):
        if(w < 0 or w > self.__G.V()):
            raise "Out of index"
        return self.__from[w] is not None

    def shortestPath(self, w):
        if(w < 0 or w > self.__G.V()):
            raise "Out of index"
        if self.__hasNegativeCycle == True:
            raise "Graph has negative Cycle!"
        if self.hasPathTo(w)==False:
            raise "Not exist path to this vertex"

        path = []
        edge = self.__from[w]
        while(edge.v() != self.__s):
            path.insert(0, edge)
            edge = self.__from[edge.v()]
        path.insert(0, edge)
        return path

    def showPath(self, w):
        if(w < 0 or w >= self.__G.V()):
            raise "Out of index"
        if(self.hasPathTo(w) == False):
            return None
        path = self.shortestPath(w)
        print "show path to %s: %s" % (w,self.__distTo[w])
        for i in range(len(path)):
            print path[i].v(),
            if i < len(path) - 1:
                print "->",
            else:
                print "-> %s" % path[i].w()










