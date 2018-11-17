#coding:utf-8

from maxHeap import MaxHeap
from maxHeap_heapify import  MaxHeap_heapify

#堆排序方法一：将数组元素逐个插入堆中，
# 然后再将堆按出堆顺序，倒序写入数组中
def heapSort1(arr):
    n = len(arr)
    maxHeap = MaxHeap(n)
    for i in range(n):
        maxHeap.insert(arr[i])

    for i in range(n-1,-1,-1):
        arr[i] = maxHeap.extractMax()

#堆排序方法二：将数组元素，按照heapify的方法，创建堆，
# 然后再将堆出堆顺序倒序写入数组
def heapSort2(arr):
    n = len(arr)
    maxHeap = MaxHeap_heapify(arr)
    for i in range(n-1,-1,-1):
        arr[i] = maxHeap.extractMax()

# 参数n为开区间，为实际处理的数组元素个数[0..n)
def __shiftDown(arr,n,k):
    while((k*2+1) <= (n-1)):
        j = k*2+1
        if(j+1 <= (n-1) and arr[j+1]>arr[j]):
            j = j +1
        if(arr[k]<arr[j]):
            arr[j],arr[k] = arr[k],arr[j]
            k = j
        else:
            break

#堆排序优化方法：利用heapify的方法，把当前数组处理成最大堆
#再将最大堆的最大元素，与数组最后的元素交换位置
#以上步骤重复，从而获得由小到大的数组排序
def heapSort(arr):
    n = len(arr)
    for i in range((n-1)/2,-1, -1):
        __shiftDown(arr, n, i)

    for i in range(n):
        arr[n-1-i],arr[0] = arr[0],arr[n-1-i]
        __shiftDown(arr,n-1-i, 0)


# arr1 = [9,7,2,1,3,8,6,4,5,0]
# arr2 = [9,7,2,1,3,8,6,4,5,0]
# arr3 = [9,7,2,1,3,8,6,4,5,0]
# heapSort2(arr1)
# heapSort1(arr2)
# heapSort(arr3)
# print "arr1",arr1
# print "arr2",arr2
# print "arr3",arr3

#
# def heapSort1(arr):
#     n = len(arr)
#     maxheap = MaxHeap(n)
#     for i in range(n):
#         maxheap.insert(arr[i])
#
#     for i in range(n-1,-1,-1):
#         arr[i] = maxheap.extractMax()
#
# # heapify的算法
# def heapSort2(arr):
#     n = len(arr)
#     maxheap = MaxHeap_heapify(arr)
#     for i in range(n-1,-1,-1):
#         arr[i] = maxheap.extractMax()
#
# def shiftDown(arr,n,k):
#     print "shiftDown,n,k,arr",n,k,arr
#     while((2*k+1) <= (n-1)):
#         j = 2*k+1 # data[k] 和data[j]进行交换，data[j]可能是左孩子，也可能是右孩子
#         if (j+1 <= n-1 and arr[j+1] > arr[j]):
#             j = j +1
#         if (arr[k] < arr[j]):
#             arr[k], arr[j] = arr[j], arr[k]
#         k = j
#
# def heapSort(arr):
#     n = len(arr)
#     for i in range((n-1)/2,-1,-1):
#         shiftDown(arr,n, i)
#
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         shiftDown(arr,i, 0)
#
# arr = [9,7,2,1,3,8,6,4,5,0]
# heapSort(arr)
# print arr
#



