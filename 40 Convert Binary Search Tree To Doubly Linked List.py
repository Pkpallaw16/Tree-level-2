# User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''


# Function to convert a binary tree to doubly linked list.
class dll:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Solution:
    dummy = dll(-1)
    prev = dummy

    def Convert_Binary_Search_Tree_To_Doubly_Linked_List(self, node):
        if node == None:
            return
        self.Convert_Binary_Search_Tree_To_Doubly_Linked_List(node.left)
        cur = dll(node.data)
        self.prev.right = cur
        cur.left = self.prev
        self.prev = cur
        self.Convert_Binary_Search_Tree_To_Doubly_Linked_List(node.right)

    def bToDLL(self, root):
        # do Code here
        self.Convert_Binary_Search_Tree_To_Doubly_Linked_List(root)
        head = self.dummy.right
        head.left = None
        return head
