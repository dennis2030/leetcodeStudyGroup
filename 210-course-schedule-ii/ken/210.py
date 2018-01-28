class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        import collections

        edge_count = collections.defaultdict(int)
        for i in xrange(numCourses):
            edge_count[i] = 0
        for pre in prerequisites:
            edge_count[pre[0]] += 1

        ans = []
        while True:
            s = -1
            for k, v in edge_count.iteritems():
                if v == 0:
                    s = k
                    break

            if s == -1:
                break

            ans.append(s)

            del edge_count[s]
            for pre in prerequisites:
                if pre[1] == s:
                    edge_count[pre[0]] -= 1

        for k, v in edge_count.iteritems():
            if v > 0:
                return []

        return ans
