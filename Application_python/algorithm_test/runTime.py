#coding=utf-8
import time

def testFunctionRunTime(func, arr):
    startTime = time.time()
    func(arr)
    endTime = time.time()

    print "The function %s run time is %s" % (func.__name__,endTime-startTime)

