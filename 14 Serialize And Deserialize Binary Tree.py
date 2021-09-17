import sys
class Node:
    def __init__(self, value=0):
        self.data = value
        self.children= []

def serialize_genericTree(node,str1):
    str1+=str(node.data)+"#"
    for child in node.children:
        str2=serialize_genericTree(child,str1)
    str2+="None#"
    return str2
def serialize(root):
    if root==None:
        return "None#"
    return serialize_genericTree(root,"")
def deserialize(str1):
    if str1=="None#":
        return None
    data=str1.split("#")[:-1]
    root=Node(data[0])
    st=[]
    st.append(root)
    for i in root(len(data)):
        if data[i]=="None":
            st.pop()
        else:
            nn=Node(int(data[i]))
            st[-1].children.append(nn)
            st.append(nn)
    return root