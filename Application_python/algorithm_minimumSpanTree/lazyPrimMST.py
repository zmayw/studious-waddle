#coding=utf-8

from minHeap import MiniHeap

class LazyPrimMST:

    def __init__(self, graph):
        self.__G = graph
        self.__marked = []
        self.__mst = []
        self.__mstWeight = 0
        self.__pq = MiniHeap("weight")

        for i in range(self.__G.V()):
            self.__marked.append(False)

        #MST
        self.__visit(0)
        while(self.__pq.isEmpty() == False):
            edge = self.__pq.extractMin()
            if self.__marked[edge.w()] == self.__marked[edge.v()]:
                continue
            self.__mst.append(edge)
            if self.__marked[edge.w()] == False:
                self.__visit(edge.w())
            else:
                self.__visit(edge.v())

        for i in range(len(self.__mst)):
            self.__mstWeight += self.__mst[i].weight()

    def __visit(self, v):
        if(self.__marked[v]==True):
            return #todo
        self.__marked[v] = True
        adj = self.__G.adjIterator(self.__G, v)
        edge = adj.begin()
        while(adj.end() == False):
            if(self.__marked[edge.other(v)]==False):
                self.__pq.insert(edge)
            edge = adj.next()

    def mstEdges(self):
        return self.__mst

    def result(self):
        return self.__mstWeight

        # i = 0
        # n = self.__G.V()
        # while i >= 0 and i < n:
        #     if (self.__marked[i] == True):
        #         continue
        #     adj = self.__G.adjIterator(self.__G,i)
        #     j = adj.begin()
        #     while adj.end()==False:
        #         if self.__marked[j] == False:
        #             self.__pq.insert(self.__G[j])
        #         j = adj.next()
        #     edge = self.__pq.extractMin()
        #     if (self.__marked[edge.v()]==False and self.__marked[edge.w()] == True):
        #         self.__marked[edge.v()] = True
        #     elif(self.__marked[edge.v()]==True and self.__marked[edge.w()]==False):
        #         self._marked[edge.w()] = True