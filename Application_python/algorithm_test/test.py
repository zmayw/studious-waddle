#coding=utf-8

import random
import numpy as np
import runTime
import selection_sort
import insertionSort
import mergeSort
import mergeSortOri
import bubbleSort
import quickSort,quickSort2,quickSort3ways,selectionTheIndexNum
import heapSort
import sys

sys.setrecursionlimit(100000)

data = np.random.permutation(300) #无序数组 10000(0.0779,0.0600)
print data
#data = np.arange(100000) #有序数组
data2 = data.copy()
data3 = data.copy()
data4 = data.copy()
data5 = data.copy()


data = data.tolist()
data2 = data2.tolist()
data3 = data3.tolist()
data4 = data4.tolist()
data5 = data5.tolist()
#runTime.testFunctionRunTime(selection_sort.selectionSort, data)
# runTime.testFunctionRunTime(insertionSort.insertionSort, data2)
# runTime.testFunctionRunTime(mergeSortOri.mergeSort,data3)
runTime.testFunctionRunTime(mergeSort.main_mergeSort,data4)
print "mergeSort,data4",data4[287-1]
runTime.testFunctionRunTime(selectionTheIndexNum.getTheIndexNumber,data5,287)


