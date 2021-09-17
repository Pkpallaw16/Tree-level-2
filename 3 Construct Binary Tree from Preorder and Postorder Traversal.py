class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def constructPrePost(self,pre,post,pre_st,pre_end,post_st,post_end):
        if pre_st==pre_end:
            return TreeNode(pre[pre_st])
        if pre_st>pre_end:
            return None
        root=TreeNode(pre[pre_st])
        ele=pre[pre_st+1]
        indx=post_st
        while post[indx]!=ele:
            indx+=1
        ele_count=indx-post_st+1
        root.left=self.constructPrePost(pre,post,pre_st+1,pre_st+ele_count,post_st,indx)
        root.right=self.constructPrePost(pre,post,pre_st+ele_count+1,pre_end,indx+1,post_end-1)
        return root
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        return self.constructPrePost(preorder,postorder,0,len(preorder)-1,0,len(postorder)-1)