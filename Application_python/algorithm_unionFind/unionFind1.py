#coding=utf-8

class UionFind1:

    def __init__(self,n):
        self.count = n
        self.id = []
        for i in range(n):
            self.id.append(i)

    def find(self,p):
        if (p>=0 and p<self.count):
            return self.id[p]

    def unionElements(self,p,q):
        idp = self.id[p]
        idq = self.id[q]
        for i in range(self.count):
            if self.id[i] == idp:
                self.id[i] = idq

    def isConnected(self,p,q):
        return self.find(p) == self.find(q)