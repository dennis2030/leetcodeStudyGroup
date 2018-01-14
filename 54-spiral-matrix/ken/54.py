class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if len(matrix) == 0:
            return []
        
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        
        def runSpiral(startx, starty, endx, endy):
            if len(ans) == m * n:
                return
            
            for i in xrange(starty, endy):
                ans.append(matrix[startx][i])

            for i in xrange(startx + 1, endx):
                ans.append(matrix[i][endy - 1])

            if endx - 1 > startx:
                for i in xrange(endy - 2, starty - 1, -1):
                    ans.append(matrix[endx - 1][i])

            if starty < endy - 1:
                for i in xrange(endx - 2, startx, - 1):
                    ans.append(matrix[i][starty])
            
            runSpiral(startx + 1, starty + 1, endx - 1, endy - 1)
        
        runSpiral(0, 0, m, n)
        
        return ans
    
