#coding=utf-8
class SequenceNode:
        def __init__(self, key, val):
            self.key = key
            self.value = val
            self.next = None
            self.head = None


class SequenceST:

    def __init__(self):
        self.head = SequenceNode(None,None)
        self.head.next = None
        self.count = 0

    def size(self):
        return self.count

    def siEmpty(self):
        return self.count==0

    def insert(self, key, value):
        node = self.head
        while( node is not None):
            if(node.key == key):
                node.value = value
                return
            node = node.next

        newNode = SequenceNode(key,value)
        newNode.next = self.head
        self.head = newNode
        self.count += 1


    def contain(self,key):
        node = self.head
        node = self.head.next
        i = 1
        while( node is not None):
            if key == node.key:
                return True
            node = node.next
            i = i+1
        return False

    def search(self,key):
        node = self.head
        while(node is not None):
            if key == node.key:
                return node
            node = node.next
        return None

