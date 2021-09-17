from _collections import deque
def Diagonal_order(root):
    q=deque()
    q.append(root)
    res=[]
    while len(q)>0:
        fact_size=len(q)
        lis = []
        while fact_size>0:
            factor=q.popleft()
            while factor!=None:
                lis.append(factor.val)
                if factor.left!=None:
                    q.append(factor.left)
                factor=factor.right

            fact_size-=1
        res.append(lis)
    return res