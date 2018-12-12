#coding=utf-8
from tempfile import TemporaryFile,NamedTemporaryFile

#1.
f = TemporaryFile() #该文件不能被系统查看
f.write('abcd'*1000)
f.seek(0)
print f.read(100)

#2.
ntf = NamedTemporaryFile() #该临时文件被关闭后，就自动消失了，也可以设置，关闭后不进行删除
print ntf.name
ntf = NamedTemporaryFile(delete=False)
print ntf.name