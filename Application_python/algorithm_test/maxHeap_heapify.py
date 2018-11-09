#coding=utf-8
import random
class MaxHeap_heapify:

    # def __init__(self,capacity,arr=[]):
    #     self.capacity = capacity
    #     self.data = []
    #     self.count = 0

    def __init__(self,arr):
        n = len(arr)
        self.capacity = n
        self.data = []
        for i in range(n):
            self.data.append(arr[i])
        self.count = n

        for i in range((self.count+1)/2,-1,-1):
            self.__shiftDown(i)



    def __shiftUp(self,k):
       #当前节点与父节点进行大小比较，如果小于父节点，则调换位置
        while(k > 0 and self.data[(k-1)/2] < self.data[k]):
            self.data[(k-1)/2] ,self.data[k] = self.data[k],self.data[(k-1)/2]
            k = (k-1)/2

    def __shiftDown(self, k):
        n = self.count
        while((2*k+1) <= (n-1)):
            j = 2*k+1 # data[k] 和data[j]进行交换，data[j]可能是左孩子，也可能是右孩子
            if (j+1 <= n-1 and self.data[j+1] > self.data[j]):
                j = j +1
            if (self.data[k] < self.data[j]):
                self.data[k],self.data[j] = self.data[j],self.data[k]
            k = j


    def isEmpty(self):
        return self.count == 0

    def insert(self, item):
        self.data.append(item)
        self.count = self.count +1
        self.__shiftUp(self.count-1)

    def extractMax(self):
        if self.count < 0:
            return
        ret = self.data[0]
        self.data[0],self.data[self.count-1] = self.data[self.count-1],self.data[0]
        self.count = self.count - 1
        self.__shiftDown(0)
        return ret



# n = 15
# maxHeap = MaxHeap(n)
# for i in range(n):
#     maxHeap.insert(random.randint(1, n))
# print maxHeap.data
#
# while( maxHeap.isEmpty() == False):
#     item = maxHeap.extractMax();
#     print item ,maxHeap





# a = [10,9,8,7,6,5]
# b = []
# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])
# print b
#
# c = []
# for i in range(len(a)):
#     c.insert(0,a[i])
# print c





