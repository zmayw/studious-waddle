#coding=utf-8

#实现用户的历史记录功能

from collections import deque
from random import randint
import pickle
import os


N = randint(0,100)
history = deque([],5)
def guess(k):
    if k == N:
        print "right"
        return True
    if k < N:
        print "%s is less-than N" % k
    else:
        print "%s is greater-than N" % k
    return False
if(os.path.isfile('history')):
    q0 = pickle.load(open('history'))
    print q0

while True:
    line = raw_input("please input a number:")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == "history" or  line == "h?":
        print list(history)
pickle.dump(history, open('history', 'w'))
