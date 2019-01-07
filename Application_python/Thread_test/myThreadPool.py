#coding=utf-8

import threadpool
import time

def f(a, b):
    print "f",a,b
    time.sleep(10)
    return a ** b


task_pool = threadpool.ThreadPool(3)
#方法一
#args = [([2, 2], None), ([3, 3], None), ([4, 4], None)]
#方法二
args = [(None, {"a":2, "b":2}), (None, {"a":3, "b":3}), (None, {"a":4, "b":4}), (None, {"a":5, "b":5})]
requests = threadpool.makeRequests(f, args)

for req in requests:
    task_pool.putRequest(req)
    print req.result()
task_pool.wait()


