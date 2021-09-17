class Solution:
    time = 0

    def root_to_node_path(self, node, tar):
        if node == None:
            return []
        if node.data == tar:
            bres = []
            bres.append(node)
            return bres
        lres = self.root_to_node_path(node.left, tar)
        if len(lres) > 0:
            lres.append(node)
            return lres
        rres = self.root_to_node_path(node.right, tar)
        if len(rres) > 0:
            rres.append(node)
            return rres
        return []

    def level_down(self, node, t, bolckage):
        if node == None or node == bolckage:
            return

        self.level_down(node.left, t + 1, bolckage)
        self.level_down(node.right, t + 1, bolckage)
        if t > self.time:
            self.time = t

    def minTime(self, root, target):
        # code here
        root_to_node = self.root_to_node_path(root, target)
        blokage = None
        t = 0
        for i in range(len(root_to_node)):
            self.level_down(root_to_node[i], t + i, blokage)
            blokage = root_to_node[i]
        return self.time