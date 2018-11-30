#coding=utf-8

class Edge:

    def __init__(self, a, b, w):
        self.__a = a
        self.__b = b
        self.__wt = w

    def v(self):
        return self.__a

    def w(self):
        return self.__b

    def weight(self):
        return self.__wt

    def other(self, x):
        if x == self.__a:
            return self.__b
        else:
            return self.__a
