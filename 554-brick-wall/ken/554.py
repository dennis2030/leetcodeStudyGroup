class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        n = len(wall)
        cnt = {}

        for line in wall:
            brickIdx = 0
            for i in xrange(len(line) - 1):
                brickIdx += line[i]
                line[i] = brickIdx

                if brickIdx not in cnt:
                    cnt[brickIdx] = 1
                else:
                    cnt[brickIdx] += 1

        if len(cnt) == 0:
            return n

        numLines = max(cnt.values())

        return n - numLines

a = Solution()
print a.leastBricks([[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]])

print a.leastBricks([[1],[1],[1]])
print a.leastBricks([[1,1],[2],[1,1]])
print a.leastBricks([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])