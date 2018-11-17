#coding=utf-8
import sys
import math
import random

def __partition(arr,l,r):
    random_l = random.randint(l,r)
    arr[l],arr[random_l] = arr[random_l],arr[l]
    j = l
    v = arr[l]
    for i in range(l,r+1):
        if(arr[i]<v):
            arr[i],arr[j+1] = arr[j+1],arr[i]
            j = j+1
    arr[l],arr[j] = arr[j],arr[l]
    return j

def __selection(arr,l,r,index):
    if(l == r):
        return arr[l]
    p = __partition(arr,l,r)
    if index<p:
        return __selection(arr,l,p-1,index)
    elif(index>p):
        return __selection(arr,p+1,r,index)
    elif(p==index):
        print "find the p,",arr[p]
        return arr[p]

def getTheIndexNumber(arr,index):
    n = len(arr)
    index = index -1 #数组下标从0开始
    e = __selection(arr,0,n-1,index)
    print e

a = [19,39,29,20,3,4,5,2,5,9,8,7,6,1,12,13,14]
k = 10 #第10个数
getTheIndexNumber(a,k)

