#coding=utf-8

class IndexMaxHeap:

    def __init__(self,arr):
        self.data = []
        self.arr = arr
        self.count = len(self.data)


    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def __shiftUp(self,index):
        while((index-1)/2 >=0 and (self.arr[self.data[index]] > self.arr[self.data[(index-1)/2]])):
            self.data[(index-1)/2] , self.data[index] = self.data[index], self.data[(index-1)/2]
            index = (index-1)/2

    def insert(self,item,index):
        self.data.append(index)
        self.count += 1
        self.__shiftUp(index)

    def __shiftDown(self,index):
        while((index*2+1)<=(self.count-1)):
            j = index*2+1
            if( (j+1)<(self.count-1) and self.arr[self.data[j]] < self.arr[self.data[j+1]]):
                j += 1
            if self.arr[self.data[index]] < self.arr[self.data[j]]:
                self.arr[self.data[index]],self.arr[self.data[j]] = self.arr[self.data[j]],self.arr[self.data[index]]
                index = j
            else:
                break


    def extractMax(self):
        if (self.count<0):
            return
        ret = self.arr[self.data[0]]
        self.data[0] = self.data[self.count-1]
        self.count -= 1
        self.__shiftDown(0)
        print "extractMax,self.size,self.arr,self.data",self.size,self.arr,self.data
        return ret

    def getItem(self,index):
        return self.arr[index]

    def change(self,index,newItem):
        self.arr[index] = newItem

        for i in range(self.count):
            if self.data[i] == index:
                self.__shiftUp(i)
                self.__shiftDown(i)
                return


def readDataElements(data,arr):
    newArr = []
    n = len(arr)
    for i in range(n):
        newArr.append(arr[data[i]])
    print newArr


a = [19,30,29,34,23,36,12,38,17,2,5,6,0]
indexMaxHeap = IndexMaxHeap(a)
n = len(a)
indexMaxHeap.change(5,100)
for i in range(n):
    indexMaxHeap.insert(a[i],i)

print "indexMaxHeap.dat",indexMaxHeap.data
readDataElements(indexMaxHeap.data,a)
print indexMaxHeap.arr
print indexMaxHeap.size()



# c = []
# for i in range(n):
#    c.insert(0,indexMaxHeap.extractMax())
# print c
# print indexMaxHeap.size()
# print indexMaxHeap.isEmpty()

