#coding=utf-8

#某项目中，我们的代码使用了三个不同库中的图形类，Circle, Triangle,Rectangle
#他们都有一个获取图形面积的接口方法，但接口名称不同
#我们可以实现一个统一的获取面积的函数，使用每种方法名进行尝试
#调用相应类的接口

#方法
#1.使用内置函数getattr，通过名字在实例上获取方法对象，然后调用
#2.使用标准库operator下的methodcaller函数调用

class Circle(object):

    def __init__(self,r):
        self.r = r

    def area(self):
        return self.r * self.r * 3.14

class Triangle(object):

    def __init__(self,l,w,h):
        self.l = l
        self.w = w
        self.h = h

    def get_area(self):
        return (self.l * self.w)/2

class Rectangle(object):

    def __init__(self,l,w):
        self.l = l
        self.w = w

    def getArea(self):
        return self.l * self.w


def getArea(shape):
    for name in ('area', 'get_area', 'getArea'):
        f = getattr(shape, name, None)
        if f:
            return f()

shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(6, 4)

shapes = [shape1, shape2, shape3]
print map(getArea,shapes)

#方法2,暂时没有想通是如何解决的
from operator import methodcaller
s = 'abc123abc456'
print s.find('abc',4)
print methodcaller('find','abc',4)(s)
# def getArea2(shape):
#     for name in ('area', 'get_area', 'getArea'):
#         f = methodcaller(name)
#         print name, shape, f
#         if f:
#             return f(shape)
#
# print map(getArea2,shapes)
