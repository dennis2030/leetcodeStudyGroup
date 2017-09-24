class Solution(object):
    
    def init(self, triangle):
        self.triangle = triangle
        self.max_len = len(triangle)
        self.calculated = []
        for i in xrange(1, self.max_len + 1):
            self.calculated.append([None] * i)
        
    def findMin(self, row, col):
        if row >= self.max_len:
            return 0
        if self.calculated[row][col] != None:
            return self.calculated[row][col]
        
        left = self.findMin(row + 1, col)
        right = self.findMin(row + 1, col + 1)
        
        self.calculated[row][col] = min(left, right) + self.triangle[row][col]
        return self.calculated[row][col]
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.init(triangle)
        return self.findMin(0, 0)
        
