# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        visited_nodes = dict()
        def visit_node(node):
            if node.label in visited_nodes:
                return visited_nodes[node.label]
            new_node = UndirectedGraphNode(node.label)
            visited_nodes[node.label] = new_node
            new_node.neighbors = [visit_node(neighbor) for neighbor in node.neighbors]

            return new_node

        return None if not node else visit_node(node)
