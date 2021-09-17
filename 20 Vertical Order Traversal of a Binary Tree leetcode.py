import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class pair:
    def __init__(self, node=None, vlevel=0, hlevel=0):
        self.node = node
        self.vlevel = vlevel
        self.hlevel = hlevel
    def __lt__(self, other):
        return self.node.val<other.node.val
class Solution:
    def verticalTraversal(self, root):
        # User function Template for python3
        lh = 0
        rh = 0
        dic = {}
        mainq=[]
        childq=[]
        heapq.heappush(mainq,pair(root, 0))
        while len(mainq) > 0:
            while len(mainq)>0:
                rem = heapq.heappop(mainq)
                if rem.vlevel < lh:
                    lh = rem.vlevel
                elif rem.vlevel > rh:
                    rh = rem.vlevel
                if rem.vlevel in dic:
                    dic[rem.vlevel].append(rem)
                else:
                    vnode = []
                    vnode.append(rem)
                    dic[rem.vlevel] = vnode
                if rem.node.left != None:
                    heapq.heappush(childq,pair(rem.node.left, rem.vlevel - 1, rem.hlevel + 1))
                if rem.node.right != None:
                    heapq.heappush(childq,pair(rem.node.right, rem.vlevel + 1, rem.hlevel + 1))
            mainq=childq
            childq=[]
        ans = []
        for i in range(lh, rh + 1):
            lis = []
            for pr in dic[i]:
                lis.append(pr.node.val)
            ans.append(lis)
        return ans




