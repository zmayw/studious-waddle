#coding=utf-8
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

def fibonacci(n):
    if (n>=0 and n <= 1):
        print n , 1
        return 1
    item = fibonacci(n-1) + fibonacci(n-2)
    print n, item
    return item

def fibonacciCache(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]

    if n <= 1:
        return 1
    cache[n] = fibonacciCache(n-1, cache) + fibonacciCache(n-2, cache)
    return cache[n]

def fibonacciIterator(n):
    data = []
    data.insert(0, 1)
    data.insert(1, 1)
    item = 0
    for i in range(2, n):
        item = data[i-1] + data[i-2]
        data.append(item)
    return item
#一共有一10个台阶的楼梯，从下面走到上面，一次只能的迈1-3步
#并且不能后退，走完这个楼梯共有多少种走法
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n-step,steps)
    return count

# fibonacci = memo(fibonacci)
# print fibonacci(10)
# print fibonacciIterator(10)
#print fibonacciCache(10)
print climb(5,(1,2,3))


