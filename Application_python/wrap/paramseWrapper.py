#coding=utf-8

#实现一个装饰器，它用来检查被装饰函数的参数类型。装饰器可以通过参数指明函数
#参数的类型，调用时如果检测出类型不匹配抛出异常
import inspect
import sys

def typeAssert(*ty_args, **ty_keyArgs):
    def decorator(func):
        #func(a,b)
        #d = {"a":int,"b":str}
        funargs = list(inspect.getargspec(func))[0]
        dtypes = []
        for i, type in enumerate(ty_args):
            item = {}
            item[funargs[i]] = type
            dtypes.append(item)

        def wrapper(*args, **kargs):
            #for arg in args:
            # arg in d, instance(arg,)d[arg]
            for index, arg in enumerate(dtypes):
                if isinstance(args[index], arg.values()[0]) == False:
                    raise TypeError("%s must be %s" % (arg,dtypes[arg]))
        return wrapper
    return decorator

@typeAssert(int, int ,int)
def f(a, b, c):
    print a, b, c

#print f(1, 's', 1)
# class Test(object):
#     cls_val = 1
#     def __init__(self):
#         self.ins_val = 10
#
# t = Test()
# print Test.__dict__
# print t.__dict__
# t.cls_val = 20
# print t.__dict__
# print Test.__dict__

# class Desc(object):
#     def __get__(self,instance,owner):
#         print "__get__..."
#         print "self:\t\t",self
#         print "instance:\t",instance
#         print "owner:\t", owner
#         print '='*40,"\n"
#
#     def __set__(self,instance,value):
#         print "__set__..."
#         print "self:\t\t",self
#         print "instance:\t",instance
#         print "value:\t",value
#         print "="*40,"\n"
#
# class TestDesc(object):
#     x = Desc()
#
# #test
# t = TestDesc()
# t.x
# print TestDesc.__dict__['x'].__get__(None,TestDesc)
# print TestDesc.__dict__

# class Desc(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         print "__get__..."
#         print "name=", self.name
#         print "="*40,"\n"
#
# class TestDesc(object):
#     x = Desc('x')
#     def __init__(self):
#         self.y = Desc("y")
#
# t = TestDesc()
# t.x
# t.y
#
# class Desc(object):
#     def __init__(self,name):
#         self.name = name
#         print "__init__():name=",self.name
#
#     def __get__(self,instance,owner):
#         print("__get__() ...")
#         return self.name
#
#     def __set__(self,instance,value):
#         self.value = value
#
# class TestDesc(object):
#     _x = Desc('x')
#     def __init__(self, x):
#         self._x = x
#
# t = TestDesc(10)
# t._x
def logger(func):
    def inner(*args, **kwargs):
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs)
    return inner

@logger
def foo1(x, y=1):
    return x * y

@logger
def foo2():
    return 2

foo1(5, 4)
foo1(1)
foo2()


