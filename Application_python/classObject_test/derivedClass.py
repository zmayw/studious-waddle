#coding=utf-8

class IntTuple(tuple):

    def __new__(cls,iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple,cls).__new__(cls,g)


    #此方法中self,由__new__方法获取到
    def __init__(self,iterable):
        #before
        super(IntTuple,self).__init__(iterable)
        #after


data = [-1, 1, 'abc', 6, ['x', 'y'], 3]
t = IntTuple(data)
print t

