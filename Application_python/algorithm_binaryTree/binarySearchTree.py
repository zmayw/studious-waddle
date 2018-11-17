#coding=utf-8

import Queue

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count

    def insert(self, key, value):
        if self.root:
            self.insertNode(self.root, key, value)
        else:
            self.root = TreeNode(key, value)

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

    def contain(self,key):
        return self.containNode(self.root,key)

    # 查看以node为根的二叉搜索树中是否包含键为key的节点
    def containNode(self,node,key):
        if node == None:
            return False
        elif( key == node.key):
            return True
        elif( key < node.key):
            return self.containNode(node.lchild,key)
        elif( key > node.key):
            return self.containNode(node.rchild,key)


    #def search(self,key):
     #   return self.searchNode(self.root,key)

    #在以node为概的二叉搜索树中查找key所对应的value
    def searchNode(self,node,key):
        if(node is None):
            return None
        elif(key == node.key):
            return node
        elif(key < node.key):
            return self.searchNode(node.lchild,key)
        elif(key > node.key):
            return self.searchNode(node.rchild,key)
        #return node.value
    #中序遍历
    def inOrder(self, node):
        if(node != None):
            self.inOrder(node.lchild)
            print node.key
            self.inOrder(node.rchild)

    #前序遍历
    def preOrder(self,node):
        if(node != None):
            print node.key
            self.preOrder(node.lchild)
            self.preOrder(node.rchild)

    #后序遍历
    def postOrder(self,node):
        if(node !=None):
            self.postOrder(node.lchild)
            self.postOrder(node.rchild)
            print node.key

    # 层序遍历
    def levelOrder(self):
        q = Queue.Queue()
        q.put(self.root)
        while(not q.empty()):
            node = q.get()
            print node.key
            if(node.lchild):
                q.put(node.lchild)
            if(node.rchild):
                q.put(node.rchild)

    #最小值
    def __minimum(self,node):
        if (node.lchild == None):
            return node

        return self.__minimum(node.lchild)

    def minimum(self):
        if self.count == 0 :
            raise "The binarySearchTree is None "
        miniNode = self.__minimum(self.root)
        return miniNode.key

    #最大值
    def maximum(self):
        if self.count == 0:
            raise "The binarySearchTree is None"
        node = self.root
        while(node.rchild):
            node = node.rchild
            if node.rchild is None:
                return node.key


    def removeMin(self):
        if(self.root):
            self.root = self.removeMiniNode(self.root)

    #删除最小值
    def removeMiniNode(self,node):
        if (node.lchild == None):
            rightNode = node.rchild
            self.count -= 1
            return rightNode
        node.lchild = self.removeMiniNode(node.lchild)
        return node

    def removeMax(self):
         if(self.root):
            self.root = self.removeMaxNode(self.root)

    #删除最大值
    def removeMaxNode(self,node):
         if(node.rchild == None):
            leftNode = node.lchild
            self.count -= 1
            return leftNode
         node.rchild = self.removeMaxNode(node.rchild)
         return node

    def removeNode(self, node, key):
        if(node is None):
            return None
        if(key > node.key):
            node.rchild = self.removeNode(node.rchild, key)
            return node
        elif( key < node.key):
            node.lchild = self.removeNode(node.lchild, key)
            return node
        elif(node.key == key):
            if node.lchild == None:
                rNode = node.rchild
                self.count -= 1
                return rNode

            if node.rchild == None:
                lNode = node.lchild
                self.count -= 1
                return lNode

            rNode = node.rchild
            lNode = node.lchild
            newNode = self.__minimum(rNode)

            node.key, node.value = newNode.key, newNode.value
            node.lchild = lNode
            node.rchild = self.removeMiniNode(rNode)
            return node

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





