class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    prev=None
    cur=None
    a=None
    b=None
    def recoverTree_helper(self,root,pointers):
        if root==None:
            return
        self.recoverTree_helper(root.left,pointers)
        if pointers[0]==None:
            #prev=None
            pointers[0]=root
        else:
            pointers[1] = root
            #prev val>cur val
            if pointers[0].val>pointers[1].val:
                #first encounter
                if pointers[3]==None:
                    pointers[2]=pointers[0]
                    pointers[3]=pointers[1]
                else:
                    #second encounter
                    pointers[3]=root
            pointers[0]=root
        self.recoverTree_helper(root.right,pointers)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pointers=[None for i in range(4)]
        self.recoverTree_helper(root,pointers)
        pointers[2].val,pointers[3].val=pointers[3].val,pointers[2].val
