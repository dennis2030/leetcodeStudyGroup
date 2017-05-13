class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #print prerequisites
        course_dep = [set() for i in xrange(numCourses)]
        for item in prerequisites:
            i, j = item
            course_dep[i].add(j)
        def dfsFindRing(course_i, dfs_visited, all_visited):
            for course_j in course_dep[course_i]:
                if course_j in dfs_visited:
                    return True
                if course_j in all_visited:
                    continue
                
                dfs_visited.add(course_j)
                all_visited.add(course_j)
                if dfsFindRing(course_j, dfs_visited, all_visited):
                    return True
                dfs_visited.discard(course_j)
            return False

        ring_found = False
        all_visited = set()
        dfs_visited = set()
        for course_i in xrange(numCourses):
            if course_i in all_visited:
                continue
            all_visited.add(course_i)
            dfs_visited.add(course_i)
            ring_found = dfsFindRing(course_i, dfs_visited, all_visited)
            if ring_found:
                break
            dfs_visited = set()

        return not ring_found
