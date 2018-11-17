#coding=utf-8

class IndexMaxHeap:

    def __init__(self):
        #self.data = []
        self.indexes = []
        self.reverse = []
        self.arr = []
        self.count = len(self.indexes)


    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def __shiftUp(self,index):
        while((index-1)/2 >=0 and (self.arr[self.indexes[index]] > self.arr[self.indexes[(index-1)/2]])):
            self.indexes[(index-1)/2] , self.indexes[index] = self.indexes[index], self.indexes[(index-1)/2]
            self.reverse[self.indexes[(index-1)/2]] = (index-1)/2
            self.reverse[self.indexes[index]] = index
            index = (index-1)/2


    def insert(self,item,index):
        self.indexes.append(index)
        self.arr.insert(index,item)
        self.count += 1
        self.reverse.insert(index,self.count-1)
        self.__shiftUp(index)

    def __shiftDown(self,index):
        while((index*2+1)<=(self.count-1)):
            j = index*2+1
            if( (j+1)<(self.count-1) and self.arr[self.indexes[j]] < self.arr[self.indexes[j+1]]):
                j += 1
            if self.arr[self.indexes[index]] < self.arr[self.indexes[j]]:
                self.arr[self.indexes[index]],self.arr[self.indexes[j]] = self.arr[self.indexes[j]],self.arr[self.indexes[index]]
                self.reverse[self.indexes[index]] = index
                self.reverse[self.indexes[j]] = j
                index = j
            else:
                break


    def extractMax(self):
        if (self.count<0):
            return
        ret = self.arr[self.indexes[0]]
        self.indexes[0] = self.indexes[self.count-1]
        self.reverse[self.indexes[0]] = 0
        self.reverse[self.indexes[self.count-1]]=0
        self.count -= 1
        self.__shiftDown(0)
        return ret

    def getItem(self,index):
        if self.contain(index)==False:
            raise "Chang index is not in indexes"
        return self.arr[index]

    def contain(self,index):
        return self.reverse[index] != 0

    def change(self,index,newItem):
        if self.contain(index)==False:
            raise "Chang index is not in indexes"
        self.arr[index] = newItem
        j = self.reverse[index]
        self.__shiftUp(j)
        self.__shiftDown(j)

        # self.arr[index] = newItem
        # for i in range(self.count):
        #     if self.data[i] == index:
        #         self.__shiftUp(i)
        #         self.__shiftDown(i)
        #         return


def readDataElements(indexes,arr):
    newArr = []
    n = len(arr)
    for i in range(n):
        newArr.append(arr[indexes[i]])
    print newArr

# a = [19,30,29,34,23,36,12,38,17,2,5,6,0]
# indexMaxHeap = IndexMaxHeap()
# n = len(a)
# for i in range(n):
#     indexMaxHeap.insert(a[i],i)
# print "the result,data   ",indexMaxHeap.indexes
# print "the result,reverse",indexMaxHeap.reverse
# print "the result arr    ",indexMaxHeap.arr
# readDataElements(indexMaxHeap.indexes,indexMaxHeap.arr)
# indexMaxHeap.change(5,100)
# print "*"*20
# print "the result,data   ",indexMaxHeap.indexes
# print "the result,reverse",indexMaxHeap.reverse
# print "the result arr    ",indexMaxHeap.arr
# readDataElements(indexMaxHeap.indexes,indexMaxHeap.arr)



