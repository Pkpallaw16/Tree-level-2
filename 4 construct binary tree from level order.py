class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
def constructIn_lvl(inord,level_ord,inord_st,inord_end):
    if len(level_ord)==0:
        return None
    root=Node(level_ord[0])
    indx=inord_st
    set1=set()
    while inord[indx]!=level_ord[0]:
        set1.add(inord[indx])
        indx+=1
    left_lvl=[]
    right_lvl=[]
    for i in range(1,len(level_ord)):
        val=level_ord[i]
        if val in set1:
            left_lvl.append(val)
        else:
            right_lvl.append(val)
    root.left=constructIn_lvl(inord,left_lvl,inord_st,indx-1)
    root.right=constructIn_lvl(inord,right_lvl,indx+1,inord_end)
    return root
def buildTree(inord ,lvlord):
    return constructIn_lvl(inord,lvlord,0,len(inord)-1)

