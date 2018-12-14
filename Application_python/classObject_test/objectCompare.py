#coding=utf-8

#有时我们希望自定义的类，实例间可以使用<,<=,>,>=,==,!=符号进行比较，我们自定义比较的行为
#例如有一个矩形的类，我们希望比较两个矩形的实例时，比较的是他们的面积

#方法
#1.重载比较符号，__lt__,__le__,__gt__,__ge__,__eq__,__ne__
#2.使用标准库下的funtools下的类装饰器total_ordering可以简化此过程
from functools import total_ordering
from abc import ABCMeta,abstractmethod

@total_ordering
class Shape(object):

    def __lt__(self,obj):
        return self.area() < obj.area()

    def __eq__(self,obj):
        return self.area() == obj.area()

    #抽像接口，子类都要实现该方法
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h



class Circle(Shape):

    def __init__(self, r):
        self.r = r


    def area(self):
        return self.r * self.r * 3.14


r1 = Rectangle(5,3)
r2 = Rectangle(4,4)
c1 = Circle(3)
print r1 < r2
print r1 <= r2
print r1 > c1
print c1 > r2
print c1 > 2