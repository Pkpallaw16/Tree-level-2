class Rpair:
    def __init__(self,withrob,withoutRob):
        self.withRob=withrob
        self.withoutRob=withoutRob
def robberyInHouse(node):
    if node==None:
        return Rpair(0,0)
    left=robberyInHouse(node.left)
    right=robberyInHouse(node.right)
    a=left.withRob
    a_=right.withRob
    b=left.withoutRob
    b_=right.withoutRob
    c=node.val
    withRob=b+b_+c
    #withoutRob=max(a+a_,a+b_,,a_+b,b+b_)
    withOutRob=max(a,b)+max(a_,b_)
    return Rpair(withRob,withOutRob)
def rob(root):
    res=robberyInHouse(root)
    return max(res.withRob,res.withoutRob)