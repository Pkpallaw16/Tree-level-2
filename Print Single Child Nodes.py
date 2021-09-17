from collections import deque
import sys
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class pair:
    def __init__(self,node,state):
        self.node=node
        self.state=state
def display(node):
    if node==None:
        return
    str1=""
    if node.left==None:
        str1 +="."
    else:
        str1 +=str(node.left.value)+""
    str1 += " <-"+str(node.value)+"-> "
    if node.right==None:
        str1 +="."
    else:
        str1 +=str(node.right.value)+""
    print(str1)
    display(node.left)
    display(node.right)
def print_single_child_nodes_Tree(node):
    if node==None:
        return None
    left_child=print_single_child_nodes_Tree(node.left)
    right_child=print_single_child_nodes_Tree(node.right)
    if left_child !=None and right_child ==None:
        print(node.left.value)
    elif left_child ==None and right_child !=None:
        print(node.right.value)
    return node
def print_single_child_nodes_Tree_2nd_approach(node,parent):
    if node==None:
        return
    if parent !=None and parent.left==node and parent.right==None:
        print(node.value)
    elif parent !=None and parent.right==node and parent.left==None:
        print(node.value)
    print_single_child_nodes_Tree_2nd_approach(node.left,node)
    print_single_child_nodes_Tree_2nd_approach(node.right,node)
def binary_tree_constructor():
    arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    stack = deque()
    root = Node(arr[0])
    root_pair = pair(root, 1)
    stack.append(root_pair)
    idx = 0
    while len(stack) > 0:
        top = stack[len(stack) - 1]
        if top.state == 1:
            idx += 1
            if arr[idx] != None:
                new_node = Node(arr[idx])
                top.node.left = new_node
                new_pair = pair(new_node, 1)
                stack.append(new_pair)
            else:
                top.node.left = None
            top.state += 1
        elif top.state == 2:
            idx += 1
            if arr[idx] != None:
                new_node = Node(arr[idx])
                top.node.right = new_node
                new_pair = pair(new_node, 1)
                stack.append(new_pair)
            else:
                top.node.right = None
            top.state += 1
        else:
            stack.pop()
    return root

root=binary_tree_constructor()
display(root)
print_single_child_nodes_Tree_2nd_approach(root,None)
print("2nd method")
print_single_child_nodes_Tree(root)










