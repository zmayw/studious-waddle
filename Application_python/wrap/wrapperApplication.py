#coding=utf-8

# 1.给函数应用做缓存
from functools import wraps

def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result
    return wrapper

@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print fib(100)

# 2.Profiler的例子
import cProfile, pstats, StringIO

def profiler(func):
    def wrapper(*args, **kargs):
        datafn = func.__name__ + ".profile"
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kargs)
        s = StringIO.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(prof, stream=s).sort_stats(sortby)
        ps.print_stats()
        print s.getvalue()
        return retval
    return wrapper

#test ,todo

#3.注册回调函数

class MyApp():
    def __init__(self):
        self.func_map = {}

    def register(self, name):
        def func_wrapper(func):
            self.func_map[name] = func
            return func
        return func_wrapper

    def call_method(self, name=None):
        func = self.func_map.get(name, None)
        if func is None:
            raise Exception("No function registered against - " + str(name))
        return func()

app = MyApp()

@app.register("/")
def main_page_func():
    return "This is the main page."

@app.register("/next_page")
def next_page_func():
    return "This is the next page."

print app.call_method("/")
print app.call_method("/next_page")

#4.给函数打日志


from functools import wraps
import time
def logger1(fn):

    @wraps(fn)
    def wrapper(*args, ** kwargs):
        ts = time.time()
        result = fn(*args, **kwargs)
        te = time.time()
        print"function  = {0}".format(fn.__name__)
        print " arguments = {0}{1}".format(args, kwargs)
        print " return = {0}".format(result)
        print " time = %.6f sec" % (te-ts)
        return result

    return wrapper

#版本2
import inspect
def get_line_number():
    return inspect.currentframe().f_back.f_back.f_lineno

def logger(loglevel):
    def log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            ts = time.time()
            result = fn(*args, **kwargs)
            te = time.time()
            print "function = "+ fn.__name__,
            print " arguments = {0}{1}".format(args,kwargs)
            print " return = {0}".format(result)
            print " time = %.6f sec" % (te - ts)
            if (loglevel == "debug"):
                print " called_from_line: " + str(get_line_number())
            return result
        return wrapper
    return log_decorator

def advance_logger(loglevel):
    def get_line_number():
        return inspect.currentframe().f_back.f_back.f_lineno

    def _basic_log(fn , result, *args, **kwargs):
        print "function = " + fn.__name__,
        print " arguments = {0}{1}".format(args, kwargs)
        print " return = {0}".format(result)

    def info_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            _basic_log(fn, result, args, kwargs)
        return wrapper

    def debug_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            ts = time.time()
            result = fn(*args, **kwargs)
            te = time.time()
            _basic_log(fn, result, args, kwargs)
            print " time = %.6f sec" % (te - ts)
            print " called_from_line : " + str(get_line_number())
        return wrapper

    if loglevel is "debug":
        return debug_log_decorator
    else:
        return info_log_decorator

@advance_logger("debug")
def multipy(x, y):
    return x * y

@advance_logger("debug1")
def sum_num(n):
    s = 0
    for i in xrange(n+1):
        s += i
    return s

print multipy(2, 10)
print sum_num(100)
print sum_num(1000)