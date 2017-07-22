# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def doClone(node, table):
            if node.label in table:
                return table[node.label]
            new = UndirectedGraphNode(node.label)
            table[node.label] = new
            for neighbor in node.neighbors:
                new.neighbors.append(doClone(neighbor, table))
            return new

        if node is None:
            return None

        table = {}
        return doClone(node, table)
