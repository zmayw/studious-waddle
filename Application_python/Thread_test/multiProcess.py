#coding=utf-8
from multiprocessing import Process
from threading import  Thread
from multiprocessing import Queue ,Pipe


def isArmstrong(n):
    a, t = [], n
    while t > 0:
        a.append(t % 10)
        t /= 10
    k = len(a)
    return sum(x ** k for x in a) == n

def findArmstrong(a,b):
    print a, b
    res = [k for k in xrange(a, b) if isArmstrong(k)]
    print "%s ~ %s:%s" % (a, b,  res)

def findByThread(*argslist):
    workers = []
    for args in argslist:
        worker = Thread(target=findArmstrong, args=args)
        workers.append(worker)
        worker.start()
        for worker in workers:
            worker.join()

def findByProcess(*argslist):
    workers = []
    for args in argslist:
        worker = Process(target=findArmstrong,args=args)
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

if __name__ == "__main__" :
    import time
    start = time.time()
    #findByProcess((20000000,25000000),(25000000,30000000))
    findByThread((20000000,25000000),(25000000,30000000))
    print time.time()-start




# q = Queue()
# q.put(1)
# print q.get()
#
# def f(q):
#     print "start"
#     print q.get()
#     print "end"
#
# Process(target=f ,args=(q,)).start()


# x = 1
# def f():
#     global x
#     x = 5
# print x
# p = Process(target=f)
# p.start()
# print x




