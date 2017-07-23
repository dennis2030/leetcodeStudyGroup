# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        m = {}
        q = []
        q.append(node)
        newRoot = UndirectedGraphNode(node.label)
        m[node.label] = newRoot

        while len(q) > 0:
            srcNode = q.pop()
            dstNode = None

            if srcNode.label not in m:
                m[srcNode.label] = UndirectedGraphNode(srcNode.label)
            dstNode = m[srcNode.label]

            for neighbor in srcNode.neighbors:
                if neighbor.label not in m:
                    m[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    q.append(neighbor)

                dstNode.neighbors.append(m[neighbor.label])

        return newRoot
