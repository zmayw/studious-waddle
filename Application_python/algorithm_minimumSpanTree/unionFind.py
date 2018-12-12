#coding=utf-8

class UnionFind:

    def __init__(self,n):
        self.__data = []
        self.__parent = []
        self.__count = n
        self.__rank = []
        for i in range(n):
            self.__parent.append(i)
            self.__rank.append(1)



    def find(self,a):
        while (a>=0 and a<self.__count) and a != self.__parent[a]:
            aRoot = self.__parent[a]
            a = self.__parent[aRoot]
        return a

    def isConnected(self,a,b):
        if (self.find(a) == self.find(b)):
            return True
        else:
            return False

    def unionElements(self,a,b):
        if a <0 or a > self.__count:
            raise "the a is out of index"
        if b <0 or b > self.__count:
            raise "the b is out of index"
        aRoot = self.find(a)
        bRoot = self.find(b)
        if aRoot == bRoot:
            return
        elif(self.__rank[aRoot] < self.__rank[bRoot]):
            self.__parent[aRoot] = bRoot
        elif(self.__rank[aRoot] > self.__rank[bRoot]):
            self.__parent[bRoot] = aRoot
        elif(self.__rank[aRoot]==self.__rank[bRoot]):
            self.__parent[aRoot] = bRoot
            self.__rank[aRoot] += 1


