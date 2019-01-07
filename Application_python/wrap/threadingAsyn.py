#coding=utf-8

#一个简单的异步执行的decorator,注意：异步处理并不简单，下面只是一个简单的示例
from threading import Thread
from functools import wraps

def async(func):
    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target=func,args=args,kwargs=kwargs)
        func_hl.start()
        return func_hl
    return async_func

if __name__ == "__main__":
    from time import sleep

    @async
    def print_somedata():
        print "starting print_somedata"
        sleep(2)
        print "pirnt_somedata: 2 sec passed"
        sleep(2)
        print "pirnt_somedata: 2 sec passed"
        sleep(2)
        print "finished print_somedata"

    def main():
        print_somedata()
        print "back in main"
        print_somedata()
        print "back in main"


    main()

