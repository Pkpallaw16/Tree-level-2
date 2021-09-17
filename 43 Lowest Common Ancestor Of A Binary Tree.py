# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    lca = None

    def Lowest_Common_Ancestor_of_bst(self, root, val1, val2):
        if root == None:
            return False
        lres = False
        rres = False
        self_check = (root == val1) or (root == val2)
        lres = self.Lowest_Common_Ancestor_of_bst(root.left, val2, val1)
        if self.lca == None:
            rres = self.Lowest_Common_Ancestor_of_bst(root.right, val1, val2)

        if (self_check and lres) or (self_check and rres) or (rres and lres):
            self.lca = root
        return self_check or lres or rres

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.Lowest_Common_Ancestor_of_bst(root, p, q)
        return self.lca

