#coding=utf-8

import sys, os, linecache

def trace(f):
    def globaltrace(frame, why, arg):
        if why == "call": return localtrace
        return None

    def localtrace(frame=1, why=2, arg=4):
        if why == "line":
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            bname = os.path.basename(filename)
            print "{}({}):{}".format(bname, lineno, linecache.getline(filename, lineno))
        return localtrace

    def _f(*args, **kwds):
        sys.settrace(globaltrace)
        result = f(*args, **kwds)
        sys.settrace(None)
        return result
    return _f


#test
import random
@trace
def xxx():
    a = 1
    print a
    print 22
    print 333
    print random.randint(1,10)



xxx()
