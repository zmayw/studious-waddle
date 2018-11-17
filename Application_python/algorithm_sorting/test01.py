#coding=utf-8

import random
import numpy as np
import runTime
import selection_sort
import insertionSort
import mergeSort
import bubbleSort
import quickSort,quickSort2,quickSort3ways
import heapSort
import sys

sys.setrecursionlimit(100000)

data = np.random.permutation(1000000) #无序数组 10000(0.0779,0.0600)
#data = np.arange(1000000) #有序数组
data2 = data.copy()
data3 = data.copy()
data4 = data.copy()
data5 = data.copy()
data6 = data.copy()
data7 = data.copy()
data8 = data.copy()
data9 = data.copy()

data = data.tolist()
data2 = data2.tolist()
data3 = data3.tolist()
data4 = data4.tolist()
data5 = data5.tolist()
data6 = data6.tolist()
data7 = data7.tolist()
data8 = data8.tolist()
data9 = data9.tolist()
# #runTime.testFunctionRunTime(selection_sort.selectionSort, data)
# #runTime.testFunctionRunTime(insertionSort.insertionSort, data2)
# #runTime.testFunctionRunTime(bubbleSort.bubbleSort,data3)
# runTime.testFunctionRunTime(mergeSort.main_mergeSort,data3)
# #runTime.testFunctionRunTime(mergeSort.main_mergeSortBU,data4)
# runTime.testFunctionRunTime(quickSort.main_quickSort,data4)
# runTime.testFunctionRunTime(quickSort2.main_quickSort2,data5)
# runTime.testFunctionRunTime(quickSort3ways.main_quickSort3ways,data6)
runTime.testFunctionRunTime(heapSort.heapSort1,data7)
runTime.testFunctionRunTime(heapSort.heapSort2,data8)
runTime.testFunctionRunTime(heapSort.heapSort,data9)

#print data
#print data2
#print data3
#print data4