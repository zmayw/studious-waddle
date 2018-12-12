#coding=utf-8

import os, stat
#一、字符串格式化
#1.startswith, endswith
data = [name for name in os.listdir('.') if name.endswith(('.sh','.py'))]
print data


#2.re.sub
import re
#把2015-12-09  替换 12/09/2015
s = '2015-12-09 lsdkskdkldls'

print re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', s)
print re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', s)

#二、字符串拼接
l = ['abc',123,45,'xyz']
#使用生成器表达式
print ''.join((str(x) for x in l))


#三、字符串左、右、中对齐
s = 'abc'
print s.ljust(10, '.')
print s.rjust(10, '.')
print s.center(10 ,'.')
print format(s,'<20')
print format(s,'>20')
print format(s,'^20')
data = {"Distcull":500.0,
 "SmallCull":0.04,
 "farclip":477,
 "lodDist":100.0,
 "trilinear":40
}
data.keys
lens = map(len,data.keys())
print lens
w = max(lens)
for k in data:
    print k.ljust(w),":",data[k]

#去掉字符串中不需要的字符
#空白字符：空格、\t,\r等

s = '---abc+++'
#1.去掉左右-+
print s.strip('-+')
#2.切片+拼接
print s[:3]+s[6:]

#3.replace
#4.re
#5.string的translate
#把a,b,c,互换成x,y,z

import string
s = 'abc1230323xyz'
string.maketrans("abcxyz",'xyzabc')
print s.translate(string.maketrans('abcxyz','xyzabc'))

s2 = 'abc\refg\n2342\t'
print s2.translate(None,'\t\r\n')
#6.unioncode  的 translate
u = u'ni hao abcd'
print unicode(u,'utf-8')