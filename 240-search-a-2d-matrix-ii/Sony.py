class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        height = len(matrix)
        if height == 0:
            return False
        width = len(matrix[0])
        if width == 0:
            return False
        found = False        
        for i in xrange(height):
            if target > matrix[i][width - 1]:
                continue
            if target < matrix[i][0] or found:
                break
            min_x = 0
            max_x = width
            while True:
                j = (min_x + max_x) // 2
                if target == matrix[i][j]:
                    found = True
                    break
                elif min_x + 1 == max_x:
                    break
                elif target < matrix[i][j]:
                    max_x = j
                else:
                    min_x = j
        return found
