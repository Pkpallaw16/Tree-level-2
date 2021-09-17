# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def constructPreIn(self,preorder,inorder,pre_start,pre_end,in_start,in_end):
        if pre_start>pre_end:
            return None
        root=TreeNode(preorder[pre_start])
        indx=in_start
        while inorder[indx]!=preorder[pre_start]:
            indx+=1
        element_count=indx-in_start
        root.left=self.constructPreIn(preorder,inorder,pre_start+1,pre_start+element_count,in_start,indx-1)
        root.right = self.constructPreIn(preorder, inorder, pre_start +element_count+1, pre_end, indx+1, in_end)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.constructPreIn(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1)
