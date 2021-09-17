# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover_helper(self, root):
        if root==None:
            return 1
        lstate=self.minCameraCover_helper(root.left)
        rstate=self.minCameraCover_helper(root.right)
        if lstate==1 and rstate==1:
            return 2
        elif lstate==2 or rstate==2:
            self.camera+=1
            return 0
        else:
            return 1
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.camera=0
        state=self.minCameraCover_helper(root)
        if state==2:
            self.camera+=1
        return self.camera