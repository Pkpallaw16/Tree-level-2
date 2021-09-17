# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def Path_Sum_In_Binary_Tree(self,root,l,tar):
        if root==None:
            return
        if root.left==None and root.right==None:
            if sum(l)+root.val==tar:
                return True
            return False
        l.append(root.val)
        lres=self.Path_Sum_In_Binary_Tree(root.left,l,tar)
        if lres==True:
            return True
        rres=self.Path_Sum_In_Binary_Tree(root.right,l,tar)
        l.pop()
        if rres==True:
            return True
        return False
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.Path_Sum_In_Binary_Tree(root,[],targetSum)

