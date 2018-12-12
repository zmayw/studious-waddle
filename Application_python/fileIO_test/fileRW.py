#coding=utf-8

s = u'您好'
#print s.encode('utf8')
f = open('py.txt','w')
f.write(s.encode('gbk'))
f.close()
f = open('py.txt','r')
t = f.read()
print t.decode('gbk')