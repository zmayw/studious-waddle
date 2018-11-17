#coding=utf-8
import random
class MaxHeap:

    def __init__(self,capacity):
        self.capacity = capacity
        self.indexes = []
        self.data = []
        self.count = 0



    def __shiftUp(self,k):
       #当前节点与父节点进行大小比较，如果小于父节点，则调换位置
        while(k > 0 and self.data[self.indexes[(k-1)/2]] < self.data[self.indexes[k]]):
            self.indexes[(k-1)/2] ,self.indexes[k] = self.indexes[k],self.indexes[(k-1)/2]
            k = (k-1)/2

    def __shiftDown(self, k):
        while((2*k+1) <= (self.count-1)):
            j = 2*k+1 # data[k] 和data[j]进行交换，data[j]可能是左孩子，也可能是右孩子
            if (j+1 <= self.count-1 and self.data[self.indexes[j+1]] > self.data[self.indexes[j]]):
                j = j +1
            if (self.data[self.indexes[k]] < self.data[self.indexes[j]]):
                self.indexes[k],self.indexes[j] = self.indexes[j],self.indexes[k]
            k = j

    def isEmpty(self):
        return self.count == 0

    def insert(self,index,item):
        if(index+1 < 1 or index + 1 > self.capacity):
            return
        self.data.append(item)
        self.indexes.append(index)
        self.count = self.count + 1
        self.__shiftUp(index)

    def extractMax(self):
        if self.count < 0:
            return
        ret = self.data[self.indexes[0]]
        self.indexes[0],self.indexes[self.count-1] = self.indexes[self.count-1],self.indexes[0]
        self.count = self.count - 1
        self.__shiftDown(0)
        return ret

    def extractMaxIndex(self):
        if self.count < 0:
            return
        ret = self.indexes[0]
        self.indexes[0],self.indexes[self.count-1] = self.indexes[self.count-1],self.indexes[0]
        self.count = self.count - 1
        self.__shiftDown(0)
        return ret

    def getItem(self,index):
        return self.data[index]

    def change(self,index,item):
        self.data[index] = item
        for j in range(self.count):
            if( self.indexes[j] == index):
                self.__shiftUp(j)
                self.__shiftDown(j)

arr = [9,7,2,1,3,8,6,4,5,0]
n = len(arr)
maxHeap = MaxHeap(n)
for i in range(n):
    maxHeap.insert(i,arr[i])
print maxHeap.data
print maxHeap.indexes

while( maxHeap.isEmpty() == False):
    item = maxHeap.extractMax()
    print item ,maxHeap.indexes




