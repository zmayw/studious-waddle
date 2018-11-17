#coding=utf-8
from binarySearchTree import *
from sequenceST import *
import time

#二、删除二叉搜索节点，测试
import random

n = 100
bst = BinarySearchTree()
#arr = [6, 4, 8, 3, 5, 7, 10]
#arr = [6, 4, 10, 3, 5, 8, 11, 7, 9, 12]
#arr=[25,14,83,8,19,64,93,49,74,97]
arr=[25,14,83,8,19,74,93,49,64,97]
n = len(arr)
for i in range(n):
    key = arr[i] #random.randint(1,n)
    arr.append(key)
    value = key
    bst.insert(key,value)


# print arr
# print "arr[3],",arr[3]
# key = arr[3]
# print "self.count=",bst.count
# bst.removeNode(bst.root,14)
# print "preOrder"
# print "bst.root,key",bst.root.key
# bst.preOrder(bst.root)
# print "self.count=",bst.count
# print "postOrder"
# bst.postOrder(bst.root)
# bst.removeMin()
# print bst.minimum()
# bst.removeMax()
# print bst.maximum()

# print bst.maximum()
# print "inOrder"
# bst.inOrder(bst.root)
# print "preOrder"
# bst.preOrder(bst.root)
# print "postOrder"
# bst.postOrder(bst.root)
# print "leveOrder"
# bst.levelOrder()



#一、链表查找和二叉搜索树查找，性能对比
# #file = open("license.txt")
# file = open("bible.txt")
# wordlines = file.readlines()
# words = []
# for line in wordlines:
#     wordArray = line.split(" ")
#     for word in wordArray:
#         if (word.strip() == word and word.strip() != ""):
#             words.append(word.lower())
# print "bible file ,words count=",len(words)
#
# startTime = time.time()
# bst = BinarySearchTree()
# i = 1
# for word in words:
#     res = bst.searchNode(bst.root,word)
#     if res is None:
#         bst.insert(word,1)
#     else:
#         res.value += 1
#
# word = "and"
# if(bst.containNode(bst.root,word)):
#     res = bst.searchNode(bst.root,word)
#     print "word in bible:res.value",res.value,res
# else:
#     print "%s word no in bible" % word
# endTime = time.time()
# print "The BST search ,time =", endTime - startTime
# print "end1"
# print "*"*30
#
# startTime2 = time.time()
# sst = SequenceST()
# i = 1
# for word in words:
#     res = sst.search(word)
#     if res is None:
#         sst.insert(word,1)
#     else:
#         res.value += 1
#
# word = "this"
# if(sst.contain(word)):
#     print "contain word is True"
#     res = sst.search(word)
# else:
#     print "%s word no in bible" % word
# endTime2 = time.time()
# print "The SST search ,time =", endTime2 - startTime2
# print "end2"
'''
测试结果
bible file ,words count= 412688
word in bible:res.value 29842 <binarySearchTree.TreeNode instance at 0x03CDEF80>
The BST search ,time = 3.52799987793
end1
******************************
contain word is True
The SST search ,time = 1186.88700008
end2
'''
