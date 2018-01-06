class Point(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def __str__(self):
        return '({0}, {1})'.format(str(self.row), str(self.col))
        
class Solution(object):
    
    def oneSpiral(self, matrix, top_left, right_bot):        
        # special cases
        if top_left.row == right_bot.row:
            return matrix[top_left.row][top_left.col:right_bot.col + 1]
        if top_left.col == right_bot.col:
            return [matrix[i][top_left.col] for i in xrange(top_left.row, right_bot.row+1)]
        
        ans = []
        # top 
        ans += matrix[top_left.row][top_left.col:right_bot.col]
        # right
        ans += [matrix[i][right_bot.col] for i in xrange(top_left.row, right_bot.row)]
        # bottom
        ans += matrix[right_bot.row][right_bot.col:top_left.col:-1]
        # left
        ans += [matrix[i][top_left.col] for i in xrange(right_bot.row, top_left.row, -1)]
        
        return ans
        
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        
        top_left = Point(0, 0)
        right_bot = Point(len(matrix) - 1, len(matrix[0]) - 1, )
        ans = []
        while True:
            if top_left.row > right_bot.row or top_left.col > right_bot.col:
                break
            ans += self.oneSpiral(matrix, top_left, right_bot)
            top_left = Point(top_left.row + 1, top_left.col + 1)
            right_bot = Point(right_bot.row - 1, right_bot.col - 1)
        return ans
        
