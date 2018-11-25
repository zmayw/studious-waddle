#coding=utf-8

class IndexMiniHeap:

    def __init__(self, capacity, keyAttribute=None):
        self.__data = []
        self.__indexes = []
        self.__count = 0
        self.__keyAttr = keyAttribute
        self.__capacity = capacity
        for i in range(capacity):
            self.__data.append(None)


    def insert(self, index, item):
        self.__data[index] = item
        self.__count += 1
        self.__indexes.append(index)

        if self.__keyAttr is not None:
            self.__shiftUpForObject(self.__count-1)
        else:
            self.__shiftUp(self.__count-1)


    def __shiftUp(self, i):
        while i > 0 and self.__data[self.__indexes[i] < self.__data[self.__indexes[(i-1)/2]]]:
            self.__indexes[i], self.__indexes[(i-1)/2] = self.__indexes[(i-1)/2], self.__indexes[i]
            i = (i-1)/2

    def __shiftUpForObject(self, i):
        while i > 0 and getattr(self.__data[self.__indexes[i]], self.__keyAttr)() < getattr(self.__data[self.__indexes[(i-1)/2]], self.__keyAttr)():
            self.__indexes[i], self.__indexes[(i-1)/2] = self.__indexes[(i-1)/2], self.__indexes[i]
            i = (i-1)/2


    def showData(self,data,indexes):
        #for i in indexes:
            #if data[i] is not None:
         #   print "%s-%s:%f" % (data[i].v(),data[i].w(),data[i].weight())
        for i in range(len(data)):
            if data[i] != None:
                print "%s-%s:%f" % (data[i].v(),data[i].w(),data[i].weight())
            else:
                print None

    def extractMin(self):
        if self.__count < 0:
            return
        ret = self.__data[self.__indexes[0]]
        self.__indexes[0] = self.__indexes[self.__count - 1]
        del self.__indexes[self.__count-1]

        self.__count -= 1
        if self.__keyAttr is not None:
            self.__shiftDownForObject(0)
        else:
            self.__shiftDown(0)
        return ret

    def extractMinIndex(self):
        if self.__count < 0:
            return
        ret = self.__indexes[0]
        self.__indexes[0] = self.__indexes[self.__count - 1]
        del self.__indexes[self.__count-1]

        self.__count -= 1
        if self.__keyAttr is not None:
            self.__shiftDownForObject(0)
        else:
            self.__shiftDown(0)
        return ret

    def __shiftDown(self, i):
        while i*2+2 < self.__count:
            j = i*2 + 1
            if self.__data[self.__indexes[i*2+1]] > self.__data[self.__indexes[i*2+2]]:
                j = i*2 + 2
            if self.__data[self.__indexes[i]] > self.__data[self.__indexes[j]]:
                self.__data[self.indexes[i]], self.__data[self.indexes[j]] = self.__data[self.indexes[j]],self.__data[self.indexes[i]]
                i = j

    def __shiftDownForObject(self, i):
        #print "self.__indexes",self.__indexes
        while i*2+2 < self.__count:
            j = i*2 + 1
            if getattr(self.__data[self.__indexes[j]], self.__keyAttr)() > getattr(self.__data[self.__indexes[j+1]], self.__keyAttr)():
                j = j + 1
            if getattr(self.__data[self.__indexes[i]], self.__keyAttr)() <= getattr(self.__data[self.__indexes[j]], self.__keyAttr)():
                break

            self.__indexes[i], self.__indexes[j] = self.__indexes[j],self.__indexes[i]
            i = j

    def getMin(self):
        if self.__count > 0:
            return self.__data[self.__indexes[0]]

    def modify(self, index, newItem):
        self.__data[index] = newItem
        for i in range(self.__count):
            if self.__indexes[i] == index:
                if self.__keyAttr is None:
                    self.__shiftUp(i)
                    self.__shiftDown(i)
                else:
                    self.__shiftUpForObject(i)
                    self.__shiftDownForObject(i)

    def isEmpty(self):
        return self.__count == 0

    # def data(self):
    #     return self.__data



