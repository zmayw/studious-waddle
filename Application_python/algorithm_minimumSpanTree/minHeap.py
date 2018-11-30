#coding=utf-8

class MinHeap(object):

    def __init__(self, keyAttribute=None):
        self.__data = []
        self.__count = 0
        self.__keyArr = keyAttribute

    def getKeyAttribute(self):
        return self.__keyArr

    def count(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def insert(self, element):
        self.__data.append(element)
        self.__count += 1
        if(self.__keyArr is not None):
            self.__shiftUpForObject(self.__count-1)
        else:
            self.__shiftUp(self.__count-1)

    def __shiftUp(self, index):
        i = index
        while i > 0:
            if self.__data[i] < self.__data[(i-1)/2]:
                self.__data[i], self.__data[(i-1)/2] = self.__data[(i-1)/2], self.__data[i]
                i = (i-1)/2
            else:
                return

    def __shiftUpForObject(self, index):
        i = index
        while i > 0:
            if getattr(self.__data[i], self.__keyArr)() < getattr(self.__data[(i-1)/2], self.__keyArr)():
                self.__data[i], self.__data[(i-1)/2] = self.__data[(i-1)/2], self.__data[i]
                i = (i-1)/2
            else:
                return

    def __shiftDown(self, i):
        while (i*2+2) < self.__count:
            k = i*2+1
            if self.__data[i*2+1] > self.__data[i*2+2]:
                k = i*2 + 2
            if self.__data[i] <= self.__data[k]:
                break
            self.__data[i], self.__data[k] = self.__data[k], self.__data[i]
            i = k

    def __shiftDownForObject(self, i):
        while (i*2+2) < self.__count:
            k = i*2+1
            if getattr(self.__data[i*2+1], self.__keyArr)() > getattr(self.__data[i*2+2], self.__keyArr)():
                k = i*2 + 2
            if getattr(self.__data[i], self.__keyArr)() <= getattr(self.__data[k], self.__keyArr)():
                break
            self.__data[i], self.__data[k] = self.__data[k], self.__data[i]
            i = k

    def extractMin(self):
        if self.__count < 0:
            pass # todo
        ret = self.__data[0]
        self.__data[0] = self.__data[self.__count - 1]
        del self.__data[self.__count-1]
        self.__count -= 1
        if( self.__keyArr is not None ):
            self.__shiftDownForObject(0)
        else:
            self.__shiftDown(0)
        return ret

    def getMin(self):
        if(self.__count > 0):
            return self.__data[0]

    def data(self):
        elements = []
        for i in range(self.__count):
            elements.append("%s-%s:%f" % (self.__data[i].v(),self.__data[i].w(),self.__data[i].weight()))
        return elements
# data = MiniHeap()
# a = [1,4,3,5,7,8,0,9,12,43]
#
# for i in range(len(a)):
#     data.insert(a[i])
#
#
# print data.count()
#
# for j in range(data.count()):
#     print data.extractMin()
