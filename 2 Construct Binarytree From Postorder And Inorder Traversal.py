# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def constructPostIn(self,post_order,inorder,post_start,post_end,in_start,in_end):
        if post_start>post_end:
            return None
        root=TreeNode(post_order[post_end])
        indx=in_start
        while inorder[indx]!=post_order[post_end]:
            indx+=1
        element_count=indx-in_start
        root.left=self.constructPostIn(post_order,inorder,post_start,post_start+element_count-1,in_start,indx-1)
        root.right = self.constructPostIn(post_order, inorder, post_start+element_count, post_end-1, indx+1, in_end)
        return root

    def buildTree(self, postorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.constructPostIn(postorder,inorder,0,len(preorder)-1,0,len(inorder)-1)
