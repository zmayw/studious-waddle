#coding=utf-8
import random

# arr[l..r]
def partition(arr,l,r):
    random_l = random.randint(l,r)
    temp = arr[l]
    arr[l] = arr[random_l]
    arr[random_l]=temp
    e = arr[l]
    j = l
    for i in range(l+1,r+1):
        if arr[i]<e:
            temp = arr[i]
            arr[i] = arr[j+1]
            arr[j+1] = temp
            j = j+1

    arr[l] = arr[j]
    arr[j] = e
    return j

def quickSort(arr,l,r):
    if (l>=r):
        return

    p = partition(arr,l,r)
    quickSort(arr,l,p-1)
    quickSort(arr,p+1,r)

def main_quickSort(arr):
    n = len(arr)
    quickSort(arr,0,n-1)

#a = [3,9,2,0,1,7,8,5,4,6]
#main_quickSort(a)
#print a


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
