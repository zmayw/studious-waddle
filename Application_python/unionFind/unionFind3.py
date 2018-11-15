#coding=utf-8
class UnionFind_optimized3:

    def __init__(self,n):
        self.count = n
        self.parent = []
        self.sz = [] #sz[i]表示以i为根的集合中的元素个数
        for i in range(n):
            self.parent.append(i)
            self.sz.append(1)

    def find(self,p):
        if (p<0 or p>self.count):
            raise "p index id out of 1-%d" % self.count
        else:
            while(self.parent[p] != p):
                p = self.parent[p]
            return self.parent[p]


    def unionElements(self,p,q):
        if (p<0 or p>self.count):
            raise "p index id out of (0-(%d-1))" % self.count
        else:
            pSize = 1
            while(self.parent[p] != p):
                p = self.parent[p]
                pSize = pSize + 1
            qSize= 1
            while(self.parent[q] !=q ):
                q = self.parent[q]
                qSize = qSize +1
            if (pSize > qSize):
                self.parent[q] = self.parent[p]
            else:
                self.parent[p] = self.parent[q]


    def isConnected(self,p,q):
        return self.find(p) == self.find(q)
