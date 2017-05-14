class Solution(object):
    import collections
    point_out_dict = {}
    hasTraversed = []
    def findCycle(self, p, traversed):
        if p in traversed:
            return True
        if p in self.hasTraversed:
            return False
        
        self.hasTraversed.append(p)
        
        copied_traversed = list(traversed)
        copied_traversed.append(p)
        
        if p not in self.point_out_dict:
            return False
        
        next_points = self.point_out_dict[p]
        for next in next_points:
            if self.findCycle(next, copied_traversed):
                return True
         
        return False
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.point_out_dict = {}
        self.hasTraversed = []
        
        for edge in prerequisites:
            if edge[0] not in self.point_out_dict:
                self.point_out_dict[edge[0]] = []
            self.point_out_dict[edge[0]].append(edge[1])
            
        hasCycle = False
        for key in self.point_out_dict:
            if self.findCycle(key, []):
                return False
        return True
