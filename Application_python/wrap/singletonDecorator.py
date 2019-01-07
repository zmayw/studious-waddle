#coding=utf-8

import sys

#使用装饰器实现简单的单例模式
def singleton(cls):
    instance = dict() #初始为空
    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton

#test
@singleton
class Test(object):
    pass

if __name__ == "__main__":
    t1 = Test()
    t2 = Test()

    #两者具有相同的地址
    print t1
    print t2

