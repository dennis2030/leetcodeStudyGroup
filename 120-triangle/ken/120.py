class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        current = [0 for i in xrange(len(triangle))]

        for row in triangle:
            for i in xrange(len(row) - 1, -1, -1):
                prev = 0
                if i == 0:
                    prev = current[i]
                elif i == len(row) - 1:
                    prev = current[i - 1]
                else:
                    prev = min(current[i - 1], current[i])

                current[i] = prev + row[i]

        return min(current)
