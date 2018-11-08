#coding=utf-8
import random


def swap(a,b):
    a,b = b,a
# arr[l..r]
def partition2(arr,l,r):
    print "lllllllllll partition2,l,r",l,r
    random_l = random.randint(l,r)
    arr[l],arr[random_l] = arr[random_l],arr[l]
    e = arr[l]
    j = r
    i = l+1
    print "ori l,random_l",l,random_l
    while(True):
        while( i <= r and arr[i] < e):
            i = i+1
        while( j >= l+1 and arr[j] > e ):
            j = j -1
        if (i > j ):
            break
        print "in while true ,i,j,arr[i],arr[j],arr:",i,j,arr[i],arr[j],arr
        arr[i],arr[j] = arr[j],arr[i]
        i = i+1
        j = j -1
        print "after swap,arr,i,j",arr,i,j
    print "before swap arr[l],arr[j]..",arr[l],arr[j],arr
    arr[l],arr[j] = arr[j],arr[l]
    print "after swap arr[l],arr[j]..",arr[l],arr[j],arr
    return j

def quickSort2(arr,l,r):
    if (l>=r):
        return
    p = partition2(arr,l,r)
    print "p pppp,",p
    quickSort2(arr,l,p-1)
    quickSort2(arr,p+1,r)

def main_quickSort2(arr):
    n = len(arr)
    quickSort2(arr,0,n-1)

a = [3,9,2,0,1,7,8,5,4,6]
main_quickSort2(a)
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
