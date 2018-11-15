#coding=utf-8
class UnionFind_optimized21:

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
        pRoot = self.find(p)
        qRoot = self.find(q)

        if pRoot == qRoot:
            return

        if(self.sz[pRoot<self.sz[qRoot]]):
            self.parent[pRoot] = qRoot
            self.sz[qRoot] += self.sz[pRoot]
        else:
            self.parent[qRoot] = pRoot
            self.sz[pRoot] += self.sz[qRoot]

    def isConnected(self,p,q):
        return self.find(p) == self.find(q)
