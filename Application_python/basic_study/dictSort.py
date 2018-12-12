#coding=utf-8

from random import randint

score = {x : randint(60,100) for x in 'xyzabc'}
print score
print sorted(zip(score.values(), score.keys()))
print sorted(score.items(),key = lambda x: x[1])