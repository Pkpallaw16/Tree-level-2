# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def root_to_node_path(self,node,tar):
        if node==None:
            return []
        if node==tar:
            bres=[]
            bres.append(node)
            return bres
        lres=self.root_to_node_path(node.left,tar)
        if len(lres)>0:
            lres.append(node)
            return lres
        rres = self.root_to_node_path(node.right,tar)
        if len(rres)>0:
            rres.append(node)
            return rres
        return []
    def print_k_level_down(self,node,k,bolckage,l):
        if node==None or node==bolckage:
            return
        if k==0:
            l.append(node.val)
        self.print_k_level_down(node.left,k-1,bolckage,l)
        self.print_k_level_down(node.right, k - 1, bolckage, l)
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        root_to_node=self.root_to_node_path(root,target)
        blokage=None
        res=[]
        for i in range(len(root_to_node)):
            if k-i>=0:
                self.print_k_level_down(root_to_node[i],k-i,blokage,res)
                blokage=root_to_node[i]
        return res