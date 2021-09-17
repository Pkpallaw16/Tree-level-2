class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def constructBst_uing_in(self,inoder,lo,hi):
        if lo>hi:
            return None
        mid = int((lo + hi) / 2)
        root=TreeNode(inoder[mid])
        root.left=self.constructBst_uing_in(inoder,lo,mid-1)
        root.right=self.constructBst_uing_in(inoder,mid+1,hi)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.constructBst_uing_in(nums,0,len(nums)-1)


