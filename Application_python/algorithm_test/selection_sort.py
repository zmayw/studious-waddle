# -*- coding:utf-8 -*-
import random
import numpy as np
import time
import runTime

def selectionSort(array):
    n = len(array)
    for i in range(n):
        minIndex=i
        for j in range(i+1,n):
            if(array[minIndex]> array[j]):
                minIndex=j
        tempData=array[i]
        array[i]=array[minIndex]
        array[minIndex]=tempData

#data=[8.0,6.2,2.1,1.3,1,5.0,0.7,0.4]
#selectionSort(data)







