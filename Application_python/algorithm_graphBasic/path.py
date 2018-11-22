#coding=utf-8

class Path:

    def __init__(self,graph,s):
        self.outOfRang(s,graph.V())
        self.G = graph
        self.s = s
        self.fromVertex = []
        self.visited = []

        n = self.G.V()
        for i in range(n):
            self.visited.append(False)
            self.fromVertex.append(-1)

        self.dfs(s)


    def dfs(self,v):
        self.visited[v] = True
        adj = self.G.adjIterator(self.G,v)
        i = adj.begin()
        while adj.end() == False:
            if self.visited[i] == False:
                self.fromVertex[i] = v
                self.dfs(i)
            i = adj.next()


    def hasPath(self,w):
        self.outOfRang(w,self.G.V())
        return self.visited[w]

    def path(self,w):
        p = w
        desPath = []
        while p != -1:
            desPath.append(p)
            p = self.fromVertex[p]
        pathArr = []

        for i in range(len(desPath)-1,-1,-1):
            pathArr.append(desPath[i])
        return pathArr


    def showPath(self,w):
        pathArr = []
        pathArr = self.path(w)
        n = len(pathArr)
        for i in range(n):
            print pathArr[i],
            if i<(n-1):
                print "->",
        print "\r\n"


    #[begin_index,len)
    def outOfRang(self,x,len,begin_index=0):
         if ( x < begin_index or x>= len):
            raise "The node is out of range(0-%d)" % len