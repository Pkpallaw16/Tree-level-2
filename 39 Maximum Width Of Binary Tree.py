from _collections import deque
class pair:
    def __init__(self, node=None, index=0):
        self.node = node
        self.index=index
def max_width_of_tree(root):
    q = deque()
    q.append(pair(root, 0))
    max_width=0
    while len(q) > 0:
        size=len(q)
        lm=q[-1].index
        rm=q[-1].index
        while size>0:
            rem = q.popleft()
            rm=rem.index
            if rem.node.left!=None:
                q.append(pair(rem.node.left,2*rem.index+1))
            if rem.node.right!=None:
                q.append(pair(rem.node.right,2*rem.index+2))
        width=rm-lm+1
        if width>max_width:
            max_width=width
    return max_width