#coding=utf-8
import math
#实现自底向上的迭代算法

#将arr[l...mid]  和 arr[mid+1,r]两部分进行归并
def __merge(arr, l, mid, r):
    aux = arr[l:(r+1)]
    i = l
    j = mid+1
    for k in range(l,r+1):
        if(i>mid):
            arr[k] = aux[j-l]
            j = j+1
        elif(j>r):
            arr[k] = aux[i-l]
            i = i+1
        elif(aux[j-l]<aux[i-l]):
            arr[k] = aux[j-l]
            j = j+1
        elif(aux[j-l]>=aux[i-l]):
            arr[k] = aux[i-l]
            i = i+1

def __mergeSort(arr, l, r):
    if (l >= r):
       return
    mid = (r-l)/2+l
    __mergeSort(arr, l, mid)
    __mergeSort(arr, mid+1, r)
    __merge(arr, l, mid, r)


def mergeSort_iteration(arr):
    n = len(arr)
    x = int(math.ceil(math.log(n,2)))
    for i in range(x):
        for j in range(0, n, 2**(i+1)):
            l = j
            r = min(j+2**(i+1)-1, n-1)
            __mergeSort(arr, l, r)

a=[10,9,8,7,2,6,5,3,4,15,1]
mergeSort_iteration(a)
print a
