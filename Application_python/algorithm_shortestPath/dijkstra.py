#coding=utf-8
from indexMinHeap import IndexMinHeap
from edge import Edge
class Dijkstra:

    def __init__(self, graph, s):
        self.__G = graph
        self.__s = s
        self.__marked = []
        self.__from = []
        self.__distTo = []
        n = self.__G.V()
        for i in range(n):
            self.__marked.append(False)
            self.__from.append(None)
            self.__distTo.append(None)

        self.__ipq = IndexMinHeap(n)
        #对其源点s进行初始化
        self.__distTo[s] = 0
        self.__marked[s] = True
        self.__ipq.insert(s, self.__distTo[s])
        self.__from[s] = Edge(s, s, 0.0)
        while(self.__ipq.isEmpty() == False):
            v = self.__ipq.extractMinIndex()

            #distTo[v]就是s到v的最短距离
            self.__marked[v] = True
            #对v的所有相邻节点进行更新
            adj = self.__G.adjIterator(self.__G, v)
            edge = adj.begin()
            while(adj.end() == False):
                w = edge.other(v)
                #如果从s点到w点的最短路径还没有找到
                if(self.__marked[w] == False):
                    weight = edge.weight() + self.__distTo[v]
                    #如果w点以前没有访问过
                    #或者访问过，但是通过当前的v点到w点距离更短，则进行更新
                    if(self.__from[w] == None or weight < self.__distTo[w]):
                        self.__from[w] = edge
                        self.__distTo[w] = weight
                        if self.__ipq.contain(w):
                            self.__ipq.modify(w, self.__distTo[w])
                        else:
                            self.__ipq.insert(w,self.__distTo[w])
                edge = adj.next()

    #返回从S点到W点的最短路径长度
    def shortestPathTo(self, w):
        if(w < 0 and w >= self.__G.V()):
            raise "Out of index"
        if self.hasPathTo(w):
            return self.__distTo[w]

    #判断从S点到W点是否联通
    def hasPathTo(self, w):
        if w>=0 and w < self.__G.V():
            return self.__marked[w]

    #寻找从S到W的最短路径，将整个路径经过的边返回
    def shortestPath(self, w):
        if(w < 0 or w >= self.__G.V()):
            raise "Out of index"
        if(self.hasPathTo(w) == False):
            return None

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
        print ""



