#coding=utf-8
import sys

#在python中，垃圾回收器通过引用计数来回收垃圾对象
#但某些环状数据结构（树，图。。。），存在对象间的循环引用
#比如树的父节点引用子节点，子节点也同时引用父节点
#此时同时del掉引用父子节点，两个对象不能被立即回收，该如何解决

#方法：
#使用标准库weakref，它可以创建一种能访问对象但不增加引用计数的对象

import weakref

# class A(object):
#     def __del__(self):
#         print "in A.__del__"
#
# a = A()
#
# a_wref = weakref.ref(a)
# a2 = a_wref()
# print a is a2
# print sys.getrefcount(a)
# del a
# del a2

class Data(object):
    def __init__(self, value, owner):
        self.owner = weakref.ref(owner) #弱引用，不增加函数调用计数
        self.value = value

    def __str__(self):
        return "%s's data,value is %s" % (self.owner, self.value)

    def __del__(self):
        print "in Data._del__"

class Node(object):
    def __init__(self,value):
        self.data = Data(value,self)

    def __del__(self):
        print "in Node.__del__"

node = Node(100)
del node
raw_input('wait...')