#coding=utf-8
from indexMiniHeap import IndexMiniHeap

class PrimMST:

    def __init__(self, graph):
        self.__data = []
        self.__marked = []
        self.__count = 0
        self.__G = graph
        self.__mst = []
        self.__mstWeights = 0
        n = self.__G.V()
        for i in range(n):
            self.__data.append(None)
            self.__marked.append(False)
        self.__ipq = IndexMiniHeap(n, "weight")

        self.__visit(0)
        while self.__ipq.isEmpty() == False:
            edge = self.__ipq.extractMin()

            if self.__marked[edge.v()] == self.__marked[edge.w()]:
                continue

            self.__mst.append(edge)
            self.__mstWeights += edge.weight()
            if(self.__marked[edge.v()]) == True:
                self.__visit(edge.w())
            else:
                self.__visit(edge.v())


    def __visit(self, v):
        if( self.__marked[v] == True):
            return
        self.__marked[v] = True
        adj = self.__G.adjIterator(self.__G, v)
        edge = adj.begin()
        while(adj.end() == False):
            w = edge.other(v)
            if self.__marked[w] == True:
                edge = adj.next()
                continue

            if self.__data[w] is None:
                self.__data[w] = edge
                self.__ipq.insert(w, edge)
            elif edge.weight() < self.__data[w].weight():
                self.__data[w] = edge
                self.__ipq.modify(w, edge)
            else:
                edge = adj.next()
                continue
            edge = adj.next()


    def mstEdges(self):
        return self.__mst

    def result(self):
        return self.__mstWeights