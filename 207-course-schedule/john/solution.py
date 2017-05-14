class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        counts = {}

        for edge in prerequisites:
            counts[edge[0]] = 0
            counts[edge[1]] = 0

        for edge in prerequisites:
            counts[edge[1]] += 1

        while counts:
            tops = set([node for node in counts if counts[node] == 0])
            if not tops:
                return False
            for edge in prerequisites:
                if edge[0] in tops:
                    counts[edge[1]] -= 1
            for top in tops:
                counts.pop(top)

        return True
