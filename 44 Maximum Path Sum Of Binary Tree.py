maxpath=0
def Maximum_Path_Sum_Of_Binary_Tree(root):
    global maxpath
    if root==None:
        return int(-1e9)
    lsum=Maximum_Path_Sum_Of_Binary_Tree(root.left)
    rsum=Maximum_Path_Sum_Of_Binary_Tree(root.right)
    val=max(root.val,lsum+root.val+rsum+root.val)
    maxpath=max(maxpath,val,lsum+rsum+root.val)
    return val