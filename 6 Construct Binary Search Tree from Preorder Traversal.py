import sys
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    indx=0
    def bstfrom_preorder(self,preorder, left_range, right_range):
        if self.indx>=len(preorder) or preorder[self.indx]<left_range or right_range<preorder[self.indx]:
            return None
        val=preorder[self.indx]
        self.indx+=1
        root=TreeNode(val)
        root.left=self.bstfrom_preorder(preorder,left_range,val)
        root.right=self.bstfrom_preorder(preorder,val,right_range)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.bstfrom_preorder(preorder,-sys.maxsize,sys.maxsize)
