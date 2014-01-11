# -*- coding: UTF-8 -*-
from tree import *


##Node insert
##입력 : 4- > 7 -> 3으로 삽입 & 중간 포인터 [1,2,3,4]
##출력 : keyList 3, 4, 7로 정렬 % nodeList[3,1,2,None]

testNodeSet = NodeSet(4)
testNodeSet.pointList[0] = 1
testNodeSet.pointList[1] = 2
testNodeSet.pointList[2] = 3
testNodeSet.insert(7)
testNodeSet.insert(3)

if testNodeSet.nodeList[0].key is 3 \
    and testNodeSet.pointList[0] is 3:
    print True

