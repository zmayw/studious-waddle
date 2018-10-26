#coding=utf-8
import random

def quickSort3ways(arr,l,r):
    if (l>=r):
        return
    random_l = random.randint(l,r)
    arr[l],arr[random_l] = arr[random_l],arr[l]
    e = arr[l]
    lt = l
    gt = r+1
    i = l+1
    while(i < gt):
        if( arr[i] < e):
            arr[i],arr[lt+1]= arr[lt+1],arr[i]
            lt = lt + 1
            i = i + 1
        elif(arr[i] > e):
            arr[i],arr[gt-1] =  arr[gt-1],arr[i]
            gt = gt - 1
        else:
            i = i + 1
    arr[l],arr[lt] = arr[lt],arr[l]
    quickSort3ways(arr,l,lt-1)
    quickSort3ways(arr,gt,r)

def main_quickSort3ways(arr):
    n = len(arr)
    quickSort3ways(arr,0,n-1)

a = [3,9,2,0,1,7,8,5,4,6]
main_quickSort3ways(a)
print a


#v1.0
# #coding=utf-8
# # arr[l..r]
# def partition(arr,l,r):
#     e = arr[l]
#     j = l
#     for i in range(l+1,r+1):
#         if arr[i]<e:
#             temp = arr[i]
#             arr[i] = arr[j+1]
#             arr[j+1] = temp
#             j = j+1
#
#     arr[l] = arr[j]
#     arr[j] = e
#     return j
#
# def quickSort(arr,l,r):
#     if (l>=r):
#         return
#
#     p = partition(arr,l,r)
#     quickSort(arr,l,p-1)
#     quickSort(arr,p+1,r)
#
# def main_quickSort(arr):
#     n = len(arr)
#     quickSort(arr,0,n-1)
#
# a = [3,9,2,0,1,7,8,5,4,6]
# main_quickSort(a)
# print a
