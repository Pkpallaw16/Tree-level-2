def morris_inorder_Traversal(node):
    ans=[]
    curr=node
    while curr!=None:
        leftnode=curr.left
        if leftnode!=None:
            rightMostnode=get_Right_Most_node(leftnode,curr)
            if rightMostnode.right!=curr:
                #create a thread and move toward left tree
                rightMostnode.right=curr
                curr=curr.left
            else:
                #if rightMostnode.right=curr that means left subtree
                ans.append(curr.val)
                rightMostnode.right=None
                curr=curr.right
        else:
            ans.append(curr.val)
            curr=curr.right
