# User function Template for python3
from _collections import deque
class pair:
    def __init__(self, node=None, vlevel=0):
        self.node = node
        self.vlevel = vlevel


class Solution:

    # Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root):
        # Your code here
        lh = 0
        rh = 0
        dic = {}
        q = deque()
        q.append(pair(root, 0))
        while len(q) > 0:
            rem = q.popleft()
            if rem.vlevel < lh:
                lh = rem.vlevel
            elif rem.vlevel > rh:
                rh = rem.vlevel
            if rem.vlevel in dic:
                dic[rem.vlevel].append(rem.node.data)
            else:
                vnode = []
                vnode.append(rem.node.data)
                dic[rem.vlevel] = vnode
            if rem.node.left != None:
                q.append(pair(rem.node.left, rem.vlevel - 1))
            if rem.node.right != None:
                q.append(pair(rem.node.right, rem.vlevel + 1))
        ans = []
        for i in range(lh, rh + 1):
            for ele in dic[i]:
                dic[i].sort()
                ans.append(ele)
        return ans



lh=0
rh=0
def Width_Of_Shadow_Of_Binary_Tree_2nd(root,count):
    global lh,rh
    if root==None:
        return
    if count<lh:
        lh=count
    elif count>rh:
        rh=count
    Width_Of_Shadow_Of_Binary_Tree_2nd(root.left,count-1)
    Width_Of_Shadow_Of_Binary_Tree_2nd(root.right,count+1)

def width(root):
    if root==None:
        return 0
    Width_Of_Shadow_Of_Binary_Tree_2nd(root,0)
    return rh+lh+1
def verticalOrder_2nd(root):
    global lh, rh
    w = width(root)
    lis = [None for i in range(w)]
    q = deque()
    q.append(pair(root, abs(lh)))
    while len(q) > 0:
        rem = q.popleft()
        lis[rem.vlevel] = rem.node.data
        if rem.node.left != None:
            q.append(pair(rem.node.left, rem.vlevel - 1))
        if rem.node.right != None:
            q.append(pair(rem.node.right, rem.vlevel + 1))
    return lis