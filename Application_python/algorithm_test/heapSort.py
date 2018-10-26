#coding:utf-8

from maxHeap import MaxHeap
from maxHeap_heapify import  MaxHeap_heapify

def heapSort1(arr):
    n = len(arr)
    maxheap = MaxHeap(n)
    for i in range(n):
        maxheap.insert(arr[i])

    for i in range(n-1,-1,-1):
        arr[i] = maxheap.extractMax()

# heapify的算法
def heapSort2(arr):
    n = len(arr)
    maxheap = MaxHeap_heapify(arr)
    for i in range(n-1,-1,-1):
        arr[i] = maxheap.extractMax()

def shiftDown(arr,n,k):
    while((2*k+1) <= (n-1)):
        j = 2*k+1 # data[k] 和data[j]进行交换，data[j]可能是左孩子，也可能是右孩子
        if (j+1 <= n-1 and arr[j+1] > arr[j]):
            j = j +1
        if (arr[k] < arr[j]):
            arr[k], arr[j] = arr[j], arr[k]
        k = j

def heapSort(arr):
    n = len(arr)
    for i in range((n-1)/2,-1,-1):
        shiftDown(arr,n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        shiftDown(arr,i, 0)







# arr = [9,7,2,1,3,8,6,4,5,0]
# heapSort2(arr)
# print arr




