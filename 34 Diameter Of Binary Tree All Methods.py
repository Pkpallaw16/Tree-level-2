max_dia=0
def Diameter_of_binary_tree(node):
    global max_dia
    if node==None:
        return -1
    lh=Diameter_of_binary_tree(node.left)
    rh=Diameter_of_binary_tree(node.right)
    dia = lh + rh + 2
    max_dia=max(max_dia,dia)
    return max(lh,rh)+1

class diapair:
    def __init__(self,dia=0,ht=-1):
        self.dia=dia
        self.ht=ht
def max_diameter_of_binary_tree(node):
    if node==None:
        return diapair()
    ldia=max_diameter_of_binary_tree(node.left)
    rdia=max_diameter_of_binary_tree(node.right)
    mres=diapair()
    mres.ht=max(ldia.ht,rdia.ht)+1
    mres.dia = max(ldia.ht+ rdia.ht + 2,ldia.dia,rdia.dia)
    return mres



