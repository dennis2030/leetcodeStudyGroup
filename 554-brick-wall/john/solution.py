class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edges = {}
        def addEdge(edge):
            if edge in edges:
                edges[edge] += 1
            else:
                edges[edge] = 1

        for row in wall:
            edge = 0
            for brick in row[:-1]:
                edge += brick
                addEdge(edge)

        if not edges:
            return len(wall)

        maxCount = max(edges.values())

        return len(wall) - maxCount
