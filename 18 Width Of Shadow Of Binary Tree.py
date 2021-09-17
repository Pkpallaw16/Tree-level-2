import sys
class Node:
    def __init__(self, val=0,data=0, left=None, right=None):
        self.val=val
        self.data = data
        self.left = left
        self.right = right
lindex=0
rindex=0
def Width_Of_Shadow_Of_Binary_Tree(root):
    global lindex,rindex
    if root==None:
        return
    if root.left!=None:
        root.left.data=root.data-1
        if lindex > root.left.data:
            lindex = root.left.data
        Width_Of_Shadow_Of_Binary_Tree(root.left)
    if root.right!=None:
        root.right.data=root.data+1
        if rindex < root.right.data:
            rindex = root.right.data
        Width_Of_Shadow_Of_Binary_Tree(root.right)
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