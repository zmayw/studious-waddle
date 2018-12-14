#coding=utf-8

#问题描述：
#某网络游戏中，定义了玩家类Player(id,name,status)
#每有一个在线玩家，在线服务器程序内则有一个Player的实例，当在线人数很多时，将产生大量实例（如百万级）
#如何降低这些大量实例的内存开销

#使用__slots__方法，声明实例的属性列表


class Player(object):
    def __init__(self,uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

class Player2(object):
    __slots__ = ['uid','name','stat','level']

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level



import sys
p1 = Player('0001','Jim')
p2 = Player2('0001','Jim')
print dir(p1)
print dir(p2)
print set(dir(p1)) - set(dir(p2))
print p1.__dict__
print sys.getsizeof(p1.__dict__)
p1.y = 9
print p1.__dict__
#p2.y = 9
