#coding=utf-8

student = ('jim',16,'male','jim8721@gmail.com')
#1.python中没有枚举类型，可以用常量来实现，加强可读性
NAME, AGE, SEX, EMAIL = xrange(4)
print student[NAME], student[SEX]

#2.使用标准库中collections.namedtuple替代内置tuple,namedtuple是tuple的子类
from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])
s1 = Student('jim',16,'male','jim8721@gmail.com')
print s1.name,s1.sex
print isinstance(s1,tuple)