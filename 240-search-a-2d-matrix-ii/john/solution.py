class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        pos = {
            'row': rows - 1,
            'col': 0,
        }

        while pos['row'] >= 0 and pos['col'] < cols:
            num = matrix[pos['row']][pos['col']]
            if num > target:
                pos['row'] -= 1
            elif num < target:
                pos['col'] += 1
            else:
                return True

        return False
