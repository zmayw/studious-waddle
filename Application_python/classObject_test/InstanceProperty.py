#coding=utf-8


class Attr(object):

    def __init__(self,name,type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self,instance, value):
        if not isinstance(value,self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value

    def __delete__(self,instance):
        del instance.__dict__[self.name]

class Person(object):
    name = Attr('name',str)
    age = Attr('age',int)
    height = Attr('height',float)

p = Person()
p.name = 'Bob'
p.age = 10
print p.age,p.name
p.age = 'abc'
print p.age
