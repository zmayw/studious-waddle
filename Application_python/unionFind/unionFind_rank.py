#coding=utf-8
class UnionFind_rank:

    def __init__(self,n):
        self.count = n
        self.parent = []
        self.rank = [] #rank[i]表示以i为根的集合中的层数
        for i in range(n):
            self.parent.append(i)
            self.rank.append(1)

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

        if(self.rank[pRoot<self.rank[qRoot]]):
            self.parent[pRoot] = qRoot
        elif(self.rank[pRoot>self.rank[qRoot]]):
            self.parent[qRoot] = pRoot
        else: #self.rank[pRoot]==self.rank[qRoot]
            self.parent[qRoot] = pRoot
            self.rank[pRoot] += 1


    def isConnected(self,p,q):
        return self.find(p) == self.find(q)
