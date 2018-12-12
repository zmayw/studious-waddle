#coding=utf-8

import mmap
import os

f = open('py.txt','r+b')
m = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE)
print m[0]
m[0]='7'
print m[0]
print mmap.PAGESIZE