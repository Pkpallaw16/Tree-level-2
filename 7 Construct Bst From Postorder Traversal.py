import sys
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    indx=0
    def bstfrom_postorder(self,postorder, left_range, right_range):
        if self.indx<0 or postorder[self.indx]<left_range or right_range<postorder[self.indx]:
            return None
        val=postorder[self.indx]
        self.indx-=1
        root=TreeNode(val)
        root.right = self.bstfrom_postorder(postorder, val, right_range)
        root.left=self.bstfrom_postorder(postorder,left_range,val)
        return root

    def bstFromPostorder(self, postorder: List[int]) -> Optional[TreeNode]:
        self.indx=len(postorder)-1
        return self.bstfrom_postorder(postorder,-sys.maxsize,sys.maxsize)
