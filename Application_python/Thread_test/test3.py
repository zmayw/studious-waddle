#coding=utf-8
#
# str = "  9293838  "
# import re
#
# #res = str.replace(r'/(^\s*)|(\s*$)/g', "")
# #res = re.sub(r"^\s*","",str)
# #res = re.sub(r"\s*$","",res)
# res = re.sub(r"(^\s*)|(\s*$)","",str)
# print res
# print "9293838"
import os
import sys
from multiprocessing import Process
from time import sleep
# print "The child will write text to pipe and "
# print "the parent will read the text written by child..."
#
# def sonpro(r, w):
#     print "**************"
#     os.close(r)
#     w = os.fdopen(w, 'w')
#     print "Child writing"
#     w.write("Text written by child...")
#     w.close()
#     print "Child closing"
#     sys.exit(0)
#
# if __name__ == "__main__":
#     #file descriptor r ,w for reading and writing
#     r, w = os.pipe()
#     #processid = os.fork() # os.fork只能在linux下应用，用来创建一个进程
#     p = Process(target=sonpro, args=(r, w))
#     os.close(w)
#     r = os.fdopen(r)
#     print "Parent reading"
#     str = r.read()
#     print "str,",str
#     print "text=",str
#     sys.exit(0)
#     p.start()
#     sleep(1)
#     p.join()
#     print "子进程运行结束"



#demo:
# def sonpro(hi, *listhi, **zidian):
#     print ("子进程%d"%os.getpid(),hi)
#     print ("其中列表参数为",listhi)
#     print ("元组为",zidian)
#
# if __name__ == "__main__":
#     print "父进程：%d "% os.getpid()
#     p = Process(target=sonpro,args=("hello word",[1,2,3,4,5]))
#     print "子进程将要执行"
#     p.start()
#     sleep(1)
#     p.join()
#     print "子进程已结束"

# def ExFunc(n):
#     sum = n
#     def InsFunc():
#         return sum + 1
#     return InsFunc
#
# myFunc = ExFunc(10)
# print type(myFunc),myFunc
# myAnotherFunc = ExFunc(20)
# print type(myAnotherFunc),myAnotherFunc
# print myFunc(),myAnotherFunc()
#
# def addx(x):
#     def adder(y): return x + y
#     return adder
#
# c = addx(8)
# print c
# # print c(10)
# print c(20)
#
# flist = []
# for i in range(3):
#     def foo(x,y=i):print x + y
#     flist.append(foo)

# for f in flist:
#     f(2)
# print flist
#闭包作用
#一、
# 假设棋盘大小为50*50，左上角为坐标系原点（0, 0）,我需要一个函数，接收2个参数，分别为
#方向，步长，该函数控制棋子的运动。棋子运动的新的坐标除了依赖方向和步长外
#还要根据原来所处的坐标点，用闭包就可以保持住这个棋子原来所处的坐标



origin = [0, 0] # 坐标系统原点
legal_x = [0, 50] # x轴方向的合法坐标
legal_y = [0, 50] # y轴方向的合法坐标

def create(pos=origin):
    def player(direction,step):
        #这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等
        #然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了
        new_x = pos[0] + direction[0] * step
        new_y = pos[1] + direction[1] * step
        pos[0] = new_x
        pos[1] = new_y
        #注决，此处不能写成pos = [new_x,new_y]
        return pos
    return player

player = create() #创建棋子player,起点为原点
print player([1, 0], 10) # 向x轴方向移10步
print player([0, 1], 20) # 向y轴方向移20步
print player([-1, 0], 10) # 向x轴负方向移10步

#二、
#闭包可以根据外部作用域的局部变量来得到不同的结果，这有点像一种类似配置功能的作用
#我们可以修改外部的变量，闭包根据这个变量展现出不同的功能
#比如有时我们需要对某些文件的特殊性行进行分析，先要提取出这些行

def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc
    return the_filter

filter = make_filter("print 'main thread'")
filter_result = filter("test2.py")
print filter
print filter_result