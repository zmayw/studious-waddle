#coding=utf-8

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


#arr = [8,7,6,4,2,3,1,9,5,0,11,34,39,32,15,16,17]
#bubbleSort(arr)
#print arr
