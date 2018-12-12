#coding=utf-8
from random import randint

#在一个for语句中迭代多个可迭代对象
#1.串行
math = [randint(60,100) for x in xrange(40)]
english = [randint(60,100) for x in xrange(40)]
chinese = [randint(60,100) for x in xrange(40)]
sum = []
for m,e,c in zip(math,english,chinese):
    sum.append(c + m + e)

print sum

#2.统计全学年成绩高于90分的
from itertools import chain
class1 = [randint(60,100) for x in xrange(40)]
class2 = [randint(60,100) for x in xrange(42)]
class3 = [randint(60,100) for x in xrange(44)]
students = []
for x in chain(class1, class2, class3):
    if x >= 90:
        students.append(x)
print len(students)
print students
