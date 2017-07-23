# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        from Queue import Queue
        q = Queue()
        
        if node == None:
            return None
        visited = {}
        root = UndirectedGraphNode(node.label)
        visited[node] = root
        q.put(node)
                
        while not q.empty():
            n = q.get()            
            copiedNeighbors = []
            for neighbor in n.neighbors:
                print neighbor.label
                if neighbor in visited:
                    copiedNeighbors.append(visited[neighbor])
                    continue                
                q.put(neighbor)                
                newNode = UndirectedGraphNode(neighbor.label)                
                visited[neighbor] = newNode
                copiedNeighbors.append(newNode)                
                
            visited[n].neighbors = copiedNeighbors
                    
        return root
