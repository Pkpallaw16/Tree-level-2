class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def mid(node):
    slow=node
    fast=node.right
    while fast!=None and fast.next!=None:
        slow=slow.right
        fast=fast.right.right
    return slow
root=None
def creation_bst(head):
    if head==None:
        return
    m = mid(head)
    if m.left!=None:
        m.left.right=None
        m.left=None
    head2=m.right
    if m.right!=None:
        m.right.left = None
        m.right = None

    if m!=head:
        m.left=creation_bst(head)
    m.right=creation_bst(head2)
    return m

def dll_2_bst(head):
    root=creation_bst(head)
    return root
