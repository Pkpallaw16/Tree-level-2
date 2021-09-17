# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class spair:
    def __init__(self, node, state):
        self.node = node
        self.state = state


class Codec:
    def Serialize_Tree(self, root, s):
        if root == None:
            s += "None#"
            return s
        s += (str(root.val) + "#")
        s = self.Serialize_Tree(root.left, s=s)
        s = self.Serialize_Tree(root.right, s=s)
        return s

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.Serialize_Tree(root, "")

    def deserialize(self, str1):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print(str1)
        if str1 == "None#":
            return None
        data = str1.split("#")[:-1]
        print(data)
        indx = 1
        root = TreeNode(int(data[0]))
        st = []
        st.append(spair(root, 0))
        while indx < len(data):
            if st[-1].state == 0:
                if data[indx] == "None":
                    st[-1].state += 1
                    indx += 1
                else:
                    nn = TreeNode(int(data[indx]))
                    st[-1].state += 1
                    st[-1].node.left = nn
                    st.append(spair(nn, 0))
                    indx += 1

            elif st[-1].state == 1:
                if data[indx] == "None":
                    st[-1].state += 1
                    indx += 1
                else:
                    nn = TreeNode(int(data[indx]))
                    st[-1].state += 1
                    st[-1].node.right = nn
                    st.append(spair(nn, 0))
                    indx += 1
            else:
                st.pop()
        return root

    # Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))