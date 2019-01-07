#coding=utf-8

import sys
#reload(sys)
#sys.setdefaultendcoding('utf-8')

import signal,functools

class TimeoutError(Exception):
    pass

def timeout(seconds, error_message="Function time out"):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGTERM, _handle_timeout) #signal.SIGALRM windows下没有此方法
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return functools.wraps(func)(wrapper)
    return decorated


#test
import time
@timeout(5) # 限定slowfunc如果在5s内不返回就强制抛出 TimeoutError  Exceptionxf gki
def slowfunc(sleep_time):
    time.sleep(sleep_time)

slowfunc(3)
slowfunc(10)
