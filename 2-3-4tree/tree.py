# -*- coding: UTF-8 -*-

max = 9999
class Tree():
    pass


class Node():
    def __init__(self, key):
        self.key = key
        self.frontNode = None
        self.backNode = None
        self.nodePoint = None
    def __repr__(self):
        return ("key : %r") % self.key

class NodeSet():
    def __init__(self, key):
        self.nodeList = [Node(key), max, max]
        self.pointList= [None, None, None, None]
        self.insertPosition = 1

    def isFull(self):
        if self.nodeList[2] is max:
            return False
        else:
            return True

    def insert(self, key):
        self.nodeList[self.insertPosition] = Node(key)
        self.insertPosition = self.insertPosition + 1
        self.sortAfterInsert()

        #isfull 확인

    #정렬 알고리즘
    def sortAfterInsert(self):
        position = self.insertPosition - 1
        while position is not 0:
            if self.nodeList[position].key > self.nodeList[position - 1].key:
                break
            else:
                self.swap(position-1, position)
                position = position-1

    def swap(self, position1, position2):
        #노드 위치 변경
        tmpNode = self.nodeList[position1]
        self.nodeList[position1] = self.nodeList[position2]
        self.nodeList[position2] = tmpNode

        #point변경
        tmpPoint = self.pointList[position2]
        self.pointList[position2] = self.pointList[position1]
        self.pointList[position1] = tmpPoint