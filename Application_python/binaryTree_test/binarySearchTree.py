#coding=utf-8

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count

    def insert(self,key,value):
        if self.root:
            self.insertNode(self.root, key, value)
        else:
            self.root = TreeNode(key,value)

    def insertNode(self,node,key,value):
        if node==None:
            node = TreeNode(key,value)
            self.count = self.count+1

        if(key == node.key):
            node.value = value
        elif(key < node.key):
            node.lchild = self.insertNode(node.lchild,key,value)
        else:
            node.rchild = self.insertNode(node.rchild,key,value)
        return node

    #def contain(self,key):

    # 查看以node为根的二叉搜索树中是否包含键为key的节点
    def contain(self,node,key):
        if node == None:
            return False
        elif( key == node.key):
            return True
        elif( key < node.key):
            return self.contain(node.lchild,key)
        elif( key > node.key):
            return self.contain(node.rchild,key)



    #在以node为概的二叉搜索树中查找key所对应的value
    def search(self,node,key):
        if(node == None):
            return None
        elif(key == node.key):
            print "search key==node.key,",key,node.key
            return node.value
        elif(key < node.key):
            print "search,key,node,node.lchild",key,node,node.key,node.lchild,node.rchild
            return self.search(node.lchild,key)
        elif(key > node.key):
            return self.search(node.rchild,key)
        return node

    def inOrder(self, node):
        if(node != None):
            self.inOrder(node.lchild)
            print node.key
            self.inOrder(node.lright)


    def preOrder(self,node):
        if(node != None):
            print node.key
            self.preOrder(node.lchild)
            self.preOrder(node.rchild)


    def postOrder(self,node):
        if(node !=None):
            self.postOrder(node.lchild)
            self.postOrder(node.rchild)
            print node.key

class TreeNode:

        def __init__(self,key,val,left=None,right=None,parent=None):
            self.key = key
            self.value = val
            self.lchild = left
            self.rchild = right
            self.parent = parent

        def hasLeftChild(self):
            return self.lchild

        def hasRightChild(self):
            return self.rchild

        def isLeftChild(self):
            return self.parent and self.parent.lchild == self

        def isRightChild(self):
            return self.parent and self.parent.rchild == self

        def isRoot(self):
            return not self.parent

        def isLeaf(self):
            return not (self.rchild or self.lchild)

        def hasAndChildren(self):
            return self.lchild or self.rchild






file = open("license.txt")
wordlines = file.readlines()
words = []
for line in wordlines:
    wordArray = line.split(" ")
    for word in wordArray:
        if (word.strip() == word and word.strip() != ""):
            words.append(word)

bst = BinarySearchTree()
i = 1
print "words:",words
for word in words:

    node = bst.search(bst.root,word)
    if(node == None):
        bst.insert(word,1)
    else:
        node.value = node.value + 1

print bst
print bst.count
print "bst.root,", bst.root

res = bst.search(bst.root,"and")
print res


