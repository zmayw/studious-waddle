#coding=utf-8

class FloatRange:

    def __init__(self,start,end,step):
        self.__start = start
        self.__end = end
        self.__step = step


    def __iter__(self):
        x = self.__start
        while x <= self.__end:
            yield x
            x += self.__step

    def __reversed__(self):
        x = self.__end
        while x >= self.__start:
            yield x
            x -= self.__step


# test

for x in FloatRange(1.0, 4.0, 0.5):
    print x

print ".........."
for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print x