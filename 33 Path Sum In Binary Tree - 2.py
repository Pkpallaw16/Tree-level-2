lis=[]
def Path_Sum_In_Binary_Tree(node,l,tar):
    if node==None:
        return
    if node.left==None and node.right==None:
        if sum(l)+node.data==tar:
            l.append(node.data)
            lis.append(l)
        return
    Path_Sum_In_Binary_Tree(node.left,l+[node.data],tar)
    Path_Sum_In_Binary_Tree(node.right,l+[node.data],tar)
def Path_Sum_In_Binary_Tree_2nd(node,l,tar,res):
    if node==None:
        return
    if node.left==None and node.right==None:
        if sum(l)+node.data==tar:
            duplicate=[]
            for i in l:
                duplicate.append(i)
            duplicate.append(node.data)
            res.append(duplicate)
        return
    l.append(node.data)
    Path_Sum_In_Binary_Tree(node.left,l,tar)
    Path_Sum_In_Binary_Tree(node.right,l,tar)
    l.pop()
def Path_sum_helper(node,tar):
    res=[]
    subres=[]
lis=[]
def Path_Sum_In_Binary_Tree(node,l,tar):
    if node==None:
        return
    if node.left==None and node.right==None:
        blis=[]
        blis.append(node.data)
        return blis

    left_lis=Path_Sum_In_Binary_Tree(node.left,tar)
    left_lis.append(node.data)
    right_lis=Path_Sum_In_Binary_Tree(node.right,tar)
    right_lis.append(node.data)

