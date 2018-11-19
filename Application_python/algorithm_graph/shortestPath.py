#coding=utf-8
import Queue

class ShortestPath:

    def __init__(self,graph,s):
        self.G = graph
        self.s = s
        self.fromVertex = []
        self.visited = []
        self.ord = []

        n = self.G.V()
        for i in range(n):
            self.fromVertex.append(-1)
            self.ord.append(-1)
            self.visited.append(False)

        q = Queue.Queue()

        q.put(s)
        self.visited[s] = True
        self.ord[s] = 0

        while(q.empty() == False):
            v = q.get()
            adj = self.G.adjIterator(self.G,v)
            i = adj.begin()
            while(adj.end()==False):
                if(self.visited[i]==False):
                    q.put(i)
                    self.visited[i] = True
                    self.fromVertex[i] = v
                    self.ord[i] = self.ord[v] + 1
                i = adj.next()


    def path(self,w):
        desPath = []
        p = w
        while( p != -1):
            desPath.append(p)
            p = self.fromVertex[p]

        ascPath = []
        for i in range(len(desPath)-1,-1,-1):
            ascPath.append(desPath[i])
        return ascPath

    def hasPath(self,w):
        self.outOfRang(w,self.G.V())
        return self.visited[w]

    def showPath(self,w):
        ascPath = self.path(w)
        n = len(ascPath)
        for i in range(n):
            print ascPath[i],
            if i< n-1:
                print "->",
        print "\r\n"

    #[begin_index,len)
    def outOfRang(self,x,len,begin_index=0):
         if ( x < begin_index or x>= len):
            raise "The node is out of range(0-%d)" % len
