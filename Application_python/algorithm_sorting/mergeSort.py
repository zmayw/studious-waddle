#coding=utf-8

def merge(arr, l, mid, r):
    aux = []
    for i in range(l,r+1):
        aux.append(arr[i])

    i = l
    j = mid+1
    for k in range(l,r+1):
        if ( i > mid):
            arr[k] = aux[j-l];
            j = j + 1
        elif ( j > r):
            arr[k] = aux[i-l]
            i = i+1
        elif (aux[i-l] < aux[j-l]):
            arr[k] = aux[i-l]
            i = i+1
        else:
            arr[k] = aux[j-l]
            j = j+1


def mergeSort(arr, l, r):
    if (l >= r):
        return
    mid = (l+r)/2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, r)
    if (arr[mid] > arr[mid+1]):
        merge(arr,l,mid,r)

def main_mergeSortBU(arr):
    n = len(arr)
    sz = 1
    for sz in range(sz,n,sz+sz):
        for i in range(0,sz,sz+sz):
            mergeSort(arr,i,i+sz)

def main_mergeSort(arr):
    n = len(arr)
    mergeSort(arr,0,n-1)

#a = [3,9,2,0,1,7,8,5,4,6]
#main_mergeSort(a)
#print a

#b =  [3,9,2,0,1,7,8,5,4,6]
#main_mergeSortBU(b)
#print b

