#coding=utf-8

import os
import stat
import time
#1.标准库os模块下的三个调用stat, fstat, lstat获取文件状态
# print os.stat('demo.bin')
# print os.lstat('demo.bin')
# f = open('demo.bin')
# print os.fstat(f.fileno())
s = os.stat('a.bat')
print s.st_mode # 33206
print stat.S_ISDIR(s.st_mode) #False
print stat.S_ISREG(s.st_mode) #True  普通文件
print s.st_mode & stat.S_IRUSR #S_IRUSR  判断用户读的权限，结果大于0  为真
print s.st_mode & stat.S_IXUSR #是否可执行
print time.localtime(s.st_atime)
print s.st_size

#2.标准库中os.path下的一些函数
print os.path.isdir('demo.bin'),os.path.isfile('demo.bin'),os.path.islink('demo.bin')
print os.path.getatime('demo.bin')
print os.path.getsize('demo.bin')