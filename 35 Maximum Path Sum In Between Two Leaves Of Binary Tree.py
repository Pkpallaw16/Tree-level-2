import sys
max_sum=-sys.maxsize
def Maximum_Path_Sum_In_Between_Two_Leaves(node):
    global max_sum
    if node.left==None and node.right==None:
        return node.data
    if node ==None:
        return -sys.maxsize
    lsum=Maximum_Path_Sum_In_Between_Two_Leaves(node.left)
    rsum=Maximum_Path_Sum_In_Between_Two_Leaves(node.right)
    if rsum==-sys.maxsize:
        max_sum = max(max_sum,node.data+lsum)
        return node.data+lsum
    elif lsum==-sys.maxsize:
        max_sum = max(max_sum,node.data+rsum)
        return node.data+rsum
    else:
        max_sum = max(max_sum, node.data + lsum+rsum)
        return max(lsum+node.data,rsum+node.data)