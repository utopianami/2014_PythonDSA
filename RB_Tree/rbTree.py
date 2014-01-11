# -*- coding: UTF-8 -*-
from bst import *

#rbTree.py
# node는 BST의 기본에 color추가
# 기본적인건 bst.py에 구현한 함수 활용(레드블랙트리는 bst트리의 부분집합이기 때문)
# 삽입함수와 삭제함수가 특이사항

#color
RED = 'red'
BLACK = 'black'

#Tree
class RBTree():
    def __init__(self):
        self.root = None
    def setRoot(self, root): #root 지정
        self.root = root
        root.color = BLACK

    def printTree(self):
        curNode = findMinNode(self)

        while(curNode is not  None):
            print curNode
            curNode = findSuccessor(self, curNode.key)

#node
class RBTreeNode():
    def __init__(self, key):
        self.key = key
        self.color = RED #처음 생성시 노드는 레드, (root는 블랙 )
        self.parent = None
        self.leftChild = NilNode(self)
        self.rightChild = NilNode(self)

    def __repr__(self):
        if self.parent is None:
            return "key : %r  color : %r Im' root"%(self.key, self.color)
        return "key : %r  color : %r parent : %r"%(self.key, self.color, self.parent.key)

    def getGrandParent(self):
        return self.parent.parent

    def getParent(self):
        return self.parent

    def getUncle(self): # uncle의 color 확인
        grandParent = self.getGrandParent()
        if self.parent is grandParent.leftChild:
            return grandParent.rightChild
        elif grandParent.rightChild is self.parent:
            return grandParent.leftChild

    def samePositionWithParent(self): #부모와 나의 좌우 포지션이 동일한지 확인
        grandParent = self.getGrandParent()
        if grandParent:
            if grandParent.leftChild is self.parent and self.parent.leftChild is self: #부모-좌, 자식-좌
                return True
            elif grandParent.rightChild is self.parent and self.parent.rightChild is self: #부모-우, 자식-우
                return True

            return False
        else: #'grandParent == None' root의 child인 경우
            return None

    def getSibling(self):
        if self is self.parent.leftChild:
            return self.parent.rightChild
        else:
            return self.parent.leftChild

#nilNode
class NilNode(RBTreeNode):
    def __init__(self, parent):
        self.key = None
        self.color = BLACK #nil Node의 color은 Black
        self.parent = parent
        self.leftChild = None
        self.rightChild = None


#leftRotate
def rightRotate(tree, node):
    parentNode = node.parent
    rotateNode = node.leftChild #회전중심노드의 왼쪽 노드

    if parentNode:
        if parentNode.leftChild is node: #parnetNode와 rotateNode 연결
            parentNode.leftChild = rotateNode
        elif parentNode.rightChild is node:
            parentNode.rightChild = rotateNode
    else:
        tree.setRoot(rotateNode)

    node.leftChild = rotateNode.rightChild
    rotateNode.rightChild.parent = node
    node.parent = rotateNode
    rotateNode.parent = parentNode
    rotateNode.rightChild = node


#rightRoate
def leftRotate(tree, node):
    parentNode = node.parent
    rotateNode = node.rightChild #회전중심노드의 왼쪽 노드

    if parentNode:
        if parentNode.leftChild is node: #parnetNode와 rotateNode 연결
            parentNode.leftChild = rotateNode
        elif parentNode.rightChild is node:
            parentNode.rightChild = rotateNode
    else:
        tree.setRoot(rotateNode)

    node.rightChild = rotateNode.leftChild
    rotateNode.leftChild.parent = node
    node.parent = rotateNode
    rotateNode.parent = parentNode
    rotateNode.leftChild = node

#RBTree_insert
def rbTreeInsert(tree, node):
    insertNode(tree, node)
    if node is tree.root:
        return

    while node.parent.color is RED:
        if node.getUncle().color is RED: #삼촌이 레드라면
            node.getGrandParent().color = RED
            node.parent.color = BLACK
            node.getUncle().color = BLACK
            node = node.getGrandParent()
            if node is tree.root: #방어 코드 : root까지 갈 경우 while문 조건에서 프로그램이 죽는다.
                break
        elif node.parent is node.getGrandParent().leftChild: # parent가 왼쪽
            if node.samePositionWithParent() is False: #부모와 자식의 좌우 위치가 다른 경우
                node = node.parent
                leftRotate(tree, node)
            node.parent.color = BLACK
            node.getGrandParent().color = RED
            rightRotate(tree, node.getGrandParent())

        elif node.parent is node.getGrandParent().rightChild: # parent가 오른쪽
            if node.samePositionWithParent() is False:
                node = node.parent
                rightRotate(tree, node)
            node.parent.color = BLACK
            node.getGrandParent().color = RED
            leftRotate(tree, node.getGrandParent())
    tree.root.color = BLACK #uncle이 RED인 경우 root까지 올라와서 root를 RED로 변경시킬수 있음


#RBTree_delete
def rbDelete(tree, key):
    node = searchNode(tree, key)
    deleteColor = node.color
    if node.leftChild.key is None:
        unBalancedNode = node.rightChild
        transPlant(tree, node, node.rightChild)
    elif node.rightChild.key is None:
        unBalancedNode = node.leftChild
        transPlant(tree, node, node.leftChild)
    else:
        successorNode = findSuccessor(tree, key)
        deleteColor = successorNode.color #successorNode가 삭제된 노드자리로 가기 때문에 삭제 대상은 successorNode로 변경
        unBalancedNode = successorNode.rightChild #successorNode가 삭제노드로 가면서 그 자리에 오는 노드의 밸런스를 맞춰야함
        if successorNode.parent is node:
            unBalancedNode.parent = successorNode
        else:
            transPlant(tree, successorNode, successorNode.rightChild)
            successorNode.rightChild = node.rightChild
            successorNode.rightChild.parent = successorNode
        transPlant(tree, node, successorNode)
        successorNode.leftChild = node.leftChild
        successorNode.leftChild.parent = successorNode
        successorNode.color = node.color #삭제 노드의 색으로 바꿈

    if deleteColor is BLACK:
        rbDeleteFixUp(tree, unBalancedNode)

def rbDeleteFixUp(tree, unBalancedNode):
    while unBalancedNode is not tree.root and unBalancedNode.color is BLACK:
        if unBalancedNode is unBalancedNode.parent.leftChild:
            sibling = unBalancedNode.getSibling()
            if sibling.color is RED: # sibling을 블랙으로 만든 후 밸런스 조절
                sibling.color = BLACK
                unBalancedNode.parent.color = RED
                leftRotate(tree, unBalancedNode.parent)
                sibling = unBalancedNode.getSibling()
            if sibling.leftChild.color is BLACK and sibling.rightChild.color is BLACK:
                sibling.color = RED
                unBalancedNode = unBalancedNode.parent # 양쪽모두 Balck Height를 -1을 준 후 unBalcedNode를 parent롤 지정
            else:
                if sibling.rightChild.color is BLACK:
                    sibling.leftChild.color = BLACK
                    sibling.color = RED
                    rightRotate(tree, sibling)
                    sibling = unBalancedNode.getSibling()
                sibling.color = unBalancedNode.parent.color
                unBalancedNode.parent.color = BLACK
                sibling.rightChild.color = BLACK
                leftRotate(tree, unBalancedNode.parent)
                break #이 경우에는 모든 경루의 black height가 조절되었기 때문에 종료
        else:
            sibling = unBalancedNode.getSibling()
            if sibling.color is RED:
                sibling.color = BLACK
                unBalancedNode.parent.color = RED
                rightRotate(tree, unBalancedNode.parent)
                sibling = unBalancedNode.getSibling()
            if sibling.rightChild.color is BLACK and sibling.leftChild.color is BLACK:
                sibling.color = RED
                if unBalancedNode.parent.color is RED:
                    unBalancedNode.parent.color = BLACK
                    break
                unBalancedNode = unBalancedNode.parent
            else:
                if sibling.leftChild.color is BLACK:
                    sibling.rightChild.color = BLACK
                    sibling.color = RED
                    leftRotate(tree, sibling)
                    sibling = unBalancedNode.getSibling()
                sibling.color = unBalancedNode.parent.color
                unBalancedNode.parent.color = BLACK
                sibling.leftChild.color = BLACK
                rightRotate(tree, unBalancedNode.parent)
                break
    unBalancedNode.color = BLACK



def checkRBTree(tree):
    blackHeight = 0
    node = tree.root
    while node is not None:  # blackHeight 계산
        if node.color is BLACK and node is not tree.root:
            blackHeight = blackHeight + 1
        node = node.leftChild

    if tree.root.color is not BLACK: #property1
        print "root가 black이 아닙니다."
        return False

    if checkTraversal(tree.root) is not True:
        return False

    if blackHeight is not checkBlackHeight(tree.root):
        print "blackHeight가 맞지 않다 "
        return False

    return True


def checkTraversal(node):
    if node.color is not RED and node.color is not BLACK: #property2
        print "각 노드는 red혹은 black가 아닙니다."
        print node
        return False
    if node.key is None:
        if node.color is not BLACK: #property3
            print "NIL노드가 블랙이 아니다"
            print node
            return False
    if node.color is RED: #property4
        if node.leftChild.color is not BLACK and node.rightChild.color is not BLACK:
            print "레드 노드의 자식이 블랙이 아니다"
            print node
            return False

    if node.key is not None:
        checkTraversal(node.leftChild)
        checkTraversal(node.rightChild)

    return True

def checkBlackHeight(node):
    #proerty5
    if node.key is not None: #Nill Node가 아니라면
        leftBlackHeight = checkBlackHeight(node.leftChild)
        rightBlackHeight = checkBlackHeight(node.rightChild)

    if node.key is None: #Nill Node라면 +1
        return 1

    if leftBlackHeight is not rightBlackHeight: #좌우 blackHeight가 다르다면
        print "좌우 높이가 다릅니다"
        print node.key

    if node.color is BLACK and node.parent is not None:
        return  leftBlackHeight + 1
    else:#노드가 레드라면 왼쪽혹은 오른쪽을 그대로 return
        return leftBlackHeight







