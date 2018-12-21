#coding=utf-8

str = "  9293838  "
import re

#res = str.replace(r'/(^\s*)|(\s*$)/g', "")
#res = re.sub(r"^\s*","",str)
#res = re.sub(r"\s*$","",res)
res = re.sub(r"(^\s*)|(\s*$)","",str)
print res
print "9293838"