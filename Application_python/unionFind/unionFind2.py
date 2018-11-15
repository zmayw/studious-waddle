#coding=utf-8
class UnionFind_optimized2:

    def __init__(self,n):
        self.count = n
        self.parent = []
        for i in range(n):
            self.parent.append(i)

    def find(self,p):
        if (p<0 or p>self.count):
            raise "p index id out of 1-%d" % self.count
        else:
            while(self.parent[p] != p):
                p = self.parent[p]
            return self.parent[p]

    def unionElements(self,p,q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        else:
            self.parent[qRoot] = pRoot

    def isConnected(self,p,q):
        return self.find(p) == self.find(q)
