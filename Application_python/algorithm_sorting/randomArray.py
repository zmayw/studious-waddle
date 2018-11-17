#conding=utf-8

import random
import numpy as np

# def random_int_list(start,stop,length):
#     start = int(start)
#     stop = int(stop)
#     if start>stop:
#         temp = start
#         start= stopa
#         stop = temp
#
#     if length == "":
#         length=0
#     random_list = []
#     for i in range(length):
#         random_list.append(random.randint(start,stop))
#     return random_list
#
# data = random_int_list(1,20,20)
# print data
#
#
# intArray = range(1,20)
# print intArray
# arr = np.arange(20)
# data = np.random.shuffle(arr)
# print data

data = np.random.permutation(20)
data = data.tolist()
print data
print data.__class__
