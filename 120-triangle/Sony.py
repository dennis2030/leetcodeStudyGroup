class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        height = len(triangle)
        last_line = [0] * (height + 1)
        for i in xrange(height - 1, -1, -1):
            this_line = []
            for idx in xrange(i + 1):
                this_line.append(triangle[i][idx] + min(last_line[idx], last_line[idx + 1]))
            last_line = this_line
            print i, last_line
        return last_line[0]




if __name__ == '__main__':

    sol = Solution()

    triangle = [[2],
               [3,4],
              [6,5,7],
             [4,1,8,3]]
    triangle = [[1]]
    print sol.minimumTotal(triangle)