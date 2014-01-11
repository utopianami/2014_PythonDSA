# -*- coding: UTF-8 -*-


def insertNode(tree, node):
    parentNode = tree.root
    curNode = tree.root

    if parentNode is None:
        tree.setRoot(node)
        return

    while curNode.key is not None: #curNode가 Nill이 될 경우 key값이 None
        if curNode.key >= node.key:
            parentNode = curNode
            curNode = curNode.leftChild
        else:
            parentNode = curNode
            curNode = curNode.rightChild

    node.parent = parentNode
    if node.key <= parentNode.key:
        parentNode.leftChild = node
    else:
        parentNode.rightChild = node


def searchNode(tree, key):
    curNode = tree.root
    while curNode.key is not None:
        if curNode.key is key:
            return curNode
        elif curNode.key > key:
            curNode = curNode.leftChild
        else:
            curNode = curNode.rightChild
    return None


def findMinNode(tree):
    curNode = tree.root
    while curNode.leftChild.key is not None:
        curNode = curNode.leftChild
    return curNode


def findMaxNode(tree):
    curNode = tree.root
    while curNode.rightChild.key is not None:
        curNode = curNode.rightChild
    return curNode


def findSuccessor(tree, key):
    node = searchNode(tree, key)
    if node is None or findMaxNode(tree).key is key: #최대값일 경우
        return None
    if node.rightChild.key is None: #오른쪽 자식이 없는 경우
        if node.parent.rightChild is node:
            return node.parent.parent
        return node.parent
    succesoorNode = node.rightChild
    while succesoorNode.leftChild.key is not None:
        succesoorNode = succesoorNode.leftChild
    return succesoorNode

########삭제 구현 : 삭제는 위치 삭제, 플랜트
def delete(tree, key):
    deleteNode = searchNode(tree, key)
    if deleteNode.leftChild.key is None:
        transPlant(tree, deleteNode, deleteNode.rightChild)

    elif deleteNode.rightChild.key is None:
        transPlant(tree, deleteNode, deleteNode.leftChild)

    else:
        successorNode = findSuccessor(tree, key)
        if deleteNode.rightChild is not successorNode:
            transPlant(tree, successorNode, successorNode.rightChild)
            successorNode.rightChild = deleteNode.rightChild
            successorNode.rightChild.parent = successorNode
        transPlant(tree, deleteNode, successorNode)
        successorNode.leftChild = deleteNode.leftChild
        successorNode.leftChild.parent = successorNode

def transPlant(tree, deleteNode, plantNode):
    parentNode = deleteNode.parent
    if parentNode is None:
        tree.root = plantNode
    elif parentNode.leftChild == deleteNode:
        parentNode.leftChild = plantNode
    elif parentNode.rightChild == deleteNode:
        parentNode.rightChild = plantNode
    if plantNode:
        plantNode.parent = parentNode #레드 블랙트리에서는 Nil 노드도 연결해야되기 때문에, plnatNode에 Nil이 오는 경우에도 부모노드 연결


def inOder(node):
    if node.key is not None:
        inOder(node.leftChild)
        print node
        inOder(node.rightChild)