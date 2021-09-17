from _collections import deque
import sys
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class LHelper:
    def __init__(self,node,leftRange,rightRange):
        self.parent=node
        self.leftRange=leftRange
        self.rightRange=rightRange
def Construct_bst_from_level_order(arr):
    q=deque()
    q.append(LHelper(None,-sys.maxsize,sys.maxsize))
    root=None
    for i in range(len(arr)):
        nn=Node(arr[i])
        while q[0].leftRange>= nn.data or q[0].rightRange<=nn.data:
            q.popleft()
        rem= q.popleft()
        q.append(LHelper(nn,rem.leftRange,nn.data))
        q.append(LHelper(nn,nn.data,rem.rightRange))
        if rem.parent==None:
            root=nn
        elif rem.parent.data>nn.data:
            rem.parent.left=nn
        else:
            rem.parent.right = nn
    return root
