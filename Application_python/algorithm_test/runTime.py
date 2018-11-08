#coding=utf-8
import time

def testFunctionRunTime(func, *args):
    startTime = time.time()
    func(*args)
    endTime = time.time()

    print "The function %s run time is %s" % (func.__name__,endTime-startTime)

#
# def info(func):
#     def wrapper(*args, **kargs):
#         wrapper.ncalls += 1
#         lt = localtime()
#         start = time()
#         res = func(*args,**kargs)
#         used = time()-start
#         info = {}
#         info["func"] = func.__name__
#         info["time"] = strftime('%x %X',lt)
#         info["used"] = used
#         info["ncalls"] = wrapper.ncalls
#         msg = '%(func)s->[%(time)s - %(used)s - %(ncalls)s]' % info
#         print msg
#         return res
#     wrapper.ncalls = 0
#     return wrapper
#
# #计算函数被调用的次数
# #暂不能区分多个函数的各自调用次数
# def getCallTimes1(last=[0]):
#     next = last[0] + 1
#     last[0] = next
#     return next
#
# import logging
# from time import localtime,time,strftime,sleep
# class CallingInfo(object):
#     def __init__(self,name):
#         log = logging.getLogger(name)
#         log.setLevel(logging.INFO)
#         fh = logging.FileHandler(name+'.log')
#         log.addHandler(fh)
#         log.info('Start'.center(50,'-'))
#         self.log = log
#         self.formatter = '%(func)s->[%(time)s - %(used)s - %(ncalls)s]'
#
#     def info(self,func):
#         def wrapper(*args,**kargs):
#             wrapper.ncalls += 1
#             lt = localtime()
#             start = time()
#             res = func(*args,**kargs)
#             used = time() - start
#             info = {}
#             info['func'] = func.__name__
#             info['time'] = strftime('%x %X',lt)
#             info['used'] = used
#             info['ncalls'] = wrapper.ncalls
#             msg = self.formatter % info
#             print msg
#             return res
#         wrapper.ncalls = 0
#         return wrapper
#
#
#
