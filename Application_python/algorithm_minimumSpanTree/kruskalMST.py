#coding=utf-8
from unionFind import UnionFind
from minHeap import MiniHeap

class KruskalMST:

    def __init__(self, graph):
        self.__G = graph
        n = self.__G.V()
        self.__uf = UnionFind(self.__G.E()+n)
        self.__data = []
        self.__mst = []
        self.__pq = MiniHeap("weight")
        self.createMiniHeap(self.__pq)
        self.__mstWeight = 0

        while(self.__pq.isEmpty() == False and len(self.__mst)<n):
            edge = self.__pq.extractMin()
            if(self.__uf.isConnected(edge.v(), edge.w())):
                continue
            else:
                #print "insert ,minedge===",edge.v(),edge.w(),edge.weight()
                self.__mst.append(edge)
                self.__uf.unionElements(edge.v(), edge.w())

        for i in range(len(self.__mst)):
            self.__mstWeight += self.__mst[i].weight()


    def createMiniHeap(self, pq):
        n = self.__G.V()
        for i in range(n):
            adj = self.__G.adjIterator(self.__G, i)
            edge = adj.begin()
            while adj.end() == False:
                if edge.v() < edge.w():
                    pq.insert(edge)
                edge = adj.next()

    def mstEdges(self):
        return self.__mst

    def result(self):
        return self.__mstWeight