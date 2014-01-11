# -*- coding: UTF-8 -*-
from bst import *
from rbTree import *

#main.py
#RBTree_TEST : 삽입, 삭제 테스트
#RBTree_TEST : 보조함수 테스트
#BSTTRee_TEST : 레드블랙트리는 BST의 부분집합이기 때문에 BST활용

###############################################
##############RBTREE_TEST######################
###############################################
#test방식은 checkRBTree() 함수 사용
#checkRBTree()는 레드블랙트리 조건 5가지를 확인하는 함수
print ""
print ""
print ""
print "RBTree_TEST"
print "삽입, 삭제"
print ""


#test1 insert(1)
#조건 : 삼촌이 red인경우, 부모와 삼촌의 색을 black으로 변경
testRBTree = RBTree()

rbTreeInsert(testRBTree, RBTreeNode(4))
rbTreeInsert(testRBTree,RBTreeNode(2))
rbTreeInsert(testRBTree,RBTreeNode(5))
rbTreeInsert(testRBTree,RBTreeNode(1)) # 1이 들어가는 순간 부모인 2와 삼촌인 5가 블랙으로
if checkRBTree(testRBTree):
    print "Test1 Pass"
else:
    print "test1 fail"

#test2 inert(2)
#조건 : 회전 (알로리즘 교제 13.2 예제 활용)
newRB = RBTree()
rbTreeInsert(newRB, RBTreeNode(41))
rbTreeInsert(newRB, RBTreeNode(38))
rbTreeInsert(newRB, RBTreeNode(31))
rbTreeInsert(newRB, RBTreeNode(12))
rbTreeInsert(newRB, RBTreeNode(19))
rbTreeInsert(newRB, RBTreeNode(8))
if checkRBTree(testRBTree):
    print "Test2 pass"
else:
    print "test2 fail"

#test3 insert(3)
#수업자료 슬라이드 15에 있는 노드를 모두 삽입
test3Tree = RBTree()
rbTreeInsert(test3Tree, RBTreeNode(3))
rbTreeInsert(test3Tree, RBTreeNode(7))
rbTreeInsert(test3Tree, RBTreeNode(10))
rbTreeInsert(test3Tree, RBTreeNode(12))
rbTreeInsert(test3Tree, RBTreeNode(14))
rbTreeInsert(test3Tree, RBTreeNode(16))
rbTreeInsert(test3Tree, RBTreeNode(15))
rbTreeInsert(test3Tree, RBTreeNode(17))
rbTreeInsert(test3Tree, RBTreeNode(21))
rbTreeInsert(test3Tree, RBTreeNode(19))
rbTreeInsert(test3Tree, RBTreeNode(20))
rbTreeInsert(test3Tree, RBTreeNode(23))
rbTreeInsert(test3Tree, RBTreeNode(26))
rbTreeInsert(test3Tree, RBTreeNode(41))
rbTreeInsert(test3Tree, RBTreeNode(30))
rbTreeInsert(test3Tree, RBTreeNode(28))
rbTreeInsert(test3Tree, RBTreeNode(38))
rbTreeInsert(test3Tree, RBTreeNode(35))
rbTreeInsert(test3Tree, RBTreeNode(39))
rbTreeInsert(test3Tree, RBTreeNode(47))
if checkRBTree(test3Tree):
    print "test3 Pass"
else:
    print "test3 fail"


#test4 delete(1)
#delete Case1 parent : black, sibling : black, sibling : balck-balck
test4Tree = RBTree()
rbTreeInsert(test4Tree, RBTreeNode(7))
rbTreeInsert(test4Tree, RBTreeNode(2))
rbTreeInsert(test4Tree, RBTreeNode(11))
rbTreeInsert(test4Tree, RBTreeNode(1))
rbTreeInsert(test4Tree, RBTreeNode(8))
rbTreeInsert(test4Tree, RBTreeNode(5))
rbTreeInsert(test4Tree, RBTreeNode(14))
rbTreeInsert(test4Tree, RBTreeNode(4))
rbDelete(test4Tree, 14)
if checkRBTree(test4Tree):
    print "test4 pass"
else:
    print "test4 fail"

#test5 delete(2)
#delete Case3 parent : black, sibling : black, sibling : red-balck
rbDelete(test4Tree, 1)
if checkRBTree(test4Tree):
    print "test5 pass"
else:
    print "test5 fail"

#test6 delete(3)
#delete Case2 parent : black, sibling : black, sibling : black/red-red
test6Tree = RBTree()
rbTreeInsert(test6Tree, RBTreeNode(7))
rbTreeInsert(test6Tree, RBTreeNode(2))
rbTreeInsert(test6Tree, RBTreeNode(11))
rbTreeInsert(test6Tree, RBTreeNode(1))
rbTreeInsert(test6Tree, RBTreeNode(8))
rbTreeInsert(test6Tree, RBTreeNode(5))
rbTreeInsert(test6Tree, RBTreeNode(14))
rbTreeInsert(test6Tree, RBTreeNode(4))
rbTreeInsert(test6Tree, RBTreeNode(6))
rbDelete(test6Tree, 1)
if checkRBTree(test6Tree):
    print "test6 pass"
else:
    print "test6 fail"

#test7 delete(5)
#delete Case2 parent : black, sibling : red, sibling : black - balck
test7Tree = RBTree()
rbTreeInsert(test7Tree, RBTreeNode(7))
rbTreeInsert(test7Tree, RBTreeNode(2))
rbTreeInsert(test7Tree, RBTreeNode(11))
rbTreeInsert(test7Tree, RBTreeNode(1))
rbTreeInsert(test7Tree, RBTreeNode(8))
rbTreeInsert(test7Tree, RBTreeNode(5))
rbTreeInsert(test7Tree, RBTreeNode(14))
rbTreeInsert(test7Tree, RBTreeNode(4))
rbTreeInsert(test7Tree, RBTreeNode(6))
rbDelete(test7Tree, 4)

if checkRBTree(test7Tree):
    print "test7 pass"
else:
    print "test7 fail"


###############################################
##############RBTREE_TEST######################
###############################################
print ""
print ""
print ""
print "RBTree_TEST 보조 함수 테스트"
print "rotate, samePositionWithParent"
print ""

#test1 leftRotate() 왼쪽 회전
newRBTree = RBTree()
newRBTree.setRoot(RBTreeNode(7))
insertNode(newRBTree, RBTreeNode(8)), insertNode(newRBTree, RBTreeNode(4)),insertNode(newRBTree, RBTreeNode(5))
insertNode(newRBTree, RBTreeNode(6)), insertNode(newRBTree, RBTreeNode(2)), insertNode(newRBTree, RBTreeNode(3))
insertNode(newRBTree, RBTreeNode(1))
standardNode = searchNode(newRBTree, 4)
rightRotate(newRBTree, standardNode)
if( newRBTree.root.leftChild.key == 2 and  newRBTree.root.leftChild.rightChild.key == 4
    and newRBTree.root.leftChild.rightChild.leftChild.key == 3
    and newRBTree.root.leftChild.rightChild.rightChild.key == 5):
    print "RBTree_test1 pass"

#test2 rightRotate() 오른쪽 회전
standardNode2 = searchNode(newRBTree, 2)
leftRotate(newRBTree, standardNode2)
if( newRBTree.root.leftChild.key == 4 and newRBTree.root.leftChild.leftChild.key == 2
    and newRBTree.root.leftChild.leftChild.rightChild.key == 3):
    print "RBTree_test2 pass"


#test3 samePositionWithParent() : 부모와 자식의 위치가 서로 같은지 다른지 확인하는 함수
#insert때 rotate횟수 체크에 활용
if (searchNode(newRBTree, 4).samePositionWithParent() == None
    and searchNode(newRBTree, 2).samePositionWithParent() == True
    and searchNode(newRBTree, 6).samePositionWithParent() == True
    and searchNode(newRBTree, 3).samePositionWithParent() == False):

    print "RBTree_test3 pass"


###############################################
##############BST_TEST#########################
###############################################
print ""
print ""
print ""
print "BST_TEST"
print ""

#test1 : 삽입
rbTree = RBTree()
rootNode = RBTreeNode(5)
rbTree.setRoot(rootNode)

node1 = RBTreeNode(2)
node2 = RBTreeNode(8)
insertNode(rbTree, node1)
insertNode(rbTree, node2)

if (rbTree.root.leftChild == node1 and rbTree.root.rightChild == node2
    and rbTree.root.leftChild.parent == rootNode and rbTree.root.leftChild.key == 2
    and rbTree.root.color == BLACK and rbTree.root.leftChild.color == RED
    and rbTree.root.leftChild.leftChild.color == BLACK):
    print "BST_test1 Pass"

#test2 : searchNode() 원하는 값의 노드가 있는 찾는 함수
resultNode = searchNode(rbTree, 10)
resultNode2 = searchNode(rbTree, 2)
if (resultNode == None and resultNode2 != None):
    print "BST_test2 pass"

#test3 : findMax(), & findMin() 최대, 최소값찾기
maxNode = findMaxNode(rbTree)
minNode = findMinNode(rbTree)
if (minNode.key == 2 and maxNode.key == 8):
    print "BST_test3 pass"

#test4 : findSuccessor() 순서상 다음 노드 찾기
insertNode(rbTree, RBTreeNode(4))
insertNode(rbTree, RBTreeNode(3))
successorNode = findSuccessor(rbTree, 2)
successorNode2 = findSuccessor(rbTree, 5)
if successorNode.key is 3 and successorNode2.key is 8:
    print "BST_test4 pass"

#test5 삭제
insertNode(rbTree, RBTreeNode(1))
insertNode(rbTree, RBTreeNode(9))
insertNode(rbTree, RBTreeNode(3.5))
delete(rbTree, 9)
delete(rbTree, 2)
if(rootNode.leftChild.key == 3 and rootNode.rightChild.rightChild.key == None
    and searchNode(rbTree, 9) == None and searchNode(rbTree, 2) == None
    and searchNode(rbTree, 4).leftChild.key == 3.5):
    print "BST_test5 pass"



