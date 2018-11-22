#coding=utf-8

class Component:

    def __init__(self,graph):
        self.G = graph
        self.visited = []
        self.ccount = 0
        n = self.G.V()
        self.id = []
        for i in range(n):
            self.visited.append(False)
            self.id.append(-1)

        for i in range(n):
            if(self.visited[i]==False):
                self.dfs(i)
                print "i,",i
                self.ccount += 1


    def dfs(self,v):
        self.visited[v] = True
        self.id[v] = self.ccount
        adj = (self.G).adjIterator(self.G,v)
        i = adj.begin()
        while adj.end()==False:
            if self.visited[i]==False:
                self.dfs(i)
            i = adj.next()


    def isConnected(self,v,w):
        self.outOfRang(v,self.G.V())
        self.outOfRang(w,self.G.V())
        return self.id[v] == self.id[w]

    def count(self):
        return self.ccount

    def outOfRang(self,x,len,begin_index=0):
        if ( x < begin_index or x>= len):
            raise "The node is out of range(0-%d)" % len