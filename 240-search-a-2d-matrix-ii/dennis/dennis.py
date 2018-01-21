class Solution(object):
    def canProceed(self, matrix, curr_r, curr_c, target):
        m = len(matrix)
        n = len(matrix[0])
        
        # down
        if curr_r + 1 < m and matrix[curr_r + 1][curr_c] <= target:
            return 'down'
        
        # left
        if curr_c - 1 >= 0:
            return 'left'
        
        return False
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
                
        curr_r = 0
        curr_c = n - 1
        
        while True:
            if target == matrix[curr_r][curr_c]:
                return True
            
            direction = self.canProceed(matrix, curr_r, curr_c, target)
            if direction == False:
                break
            elif direction == 'down':            
                curr_r += 1
            elif direction == 'left':
                curr_c -= 1
            else:
                print 'Unknown case'
        return False                                                
