#coding=utf-8
import time

#方法一
# def insertionSort(a):
#     n = len(a)
#     for i in range(n):
#         if i == 0:
#             continue
#         for j in range(i, 0, -1):
#             if (a[j] < a[j-1]):
#                 temp = a[j]
#                 a[j] = a[j-1]
#                 a[j-1] = temp


#方法二，优化里层循环，减少替换操作为一次，其它为赋值操作

#
# a = [2,9,0,3,8,6,7,1,4,5]
# #a = [2,0]

def insertionSort(a):
    n = len(a)
    for i in range(n):
        if i == 0:
            continue

        e = a[i]
        j = i
        for j in range(i, -1, -1):
            if e < a[j-1]:
                a[j] = a[j-1]
            else:
                break
        a[j] = e

#  选择排序
# a = [2,9,0,3,8,6,7,1,4,5]
# n = len(a)
#
# for i in range(n):
#     temp = a[i]
#     m = i
#     for j in range(i,n-1):
#         if temp > a[j+1]:
#             temp = a[j+1]
#             m = j+1
#     a[m] = a[i]
#     a[i] = temp
#
# print a