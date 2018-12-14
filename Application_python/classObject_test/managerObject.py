#coding=utf-8

#在面向对象编程中，我们把方法（函数）看作对象的接口
#直接访问对象的属性可能是不安全的，或设计上不够灵活
#但是使用调用方法在形式上不如方问属性简洁

#方法：在形式上是属性访问，但实际上调用方法
#使用property函数为类创建可管理属性，fget/fset/fdel对应相应属性访问

from math import pi

class Circle(object):

    def __init__(self,radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self,value):
        if not isinstance(value,(int,long,float)):
            raise ValueError('wrong type.')
        self.__radius = float(value)

    def getArea(self):
        return self.__radius **2 *pi

    R = property(getRadius,setRadius)

c = Circle(3.2)
print c.R
c.R = 4.5
print c.R
