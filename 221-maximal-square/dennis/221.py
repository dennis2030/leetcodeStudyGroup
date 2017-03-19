#!/usr/bin/env python2.7
class Solution(object):
    def maximalSquare(self, matrix):
        num_of_rows = len(matrix)
        num_of_cols = len(matrix[0]) if len(matrix) > 0 else 0
        if num_of_rows <= 0 or num_of_cols <= 0:
            return 0

        # tuple = (top, left, top-left)
        dist_tuples = [[None] * num_of_cols for _ in xrange(num_of_rows)]
        champion_square_root = 0
        for row_idx in xrange(num_of_rows):
            for col_idx in xrange(num_of_cols):
                is_barrier = (matrix[row_idx][col_idx] == '0')
                if is_barrier:
                    dist_tuples[row_idx][col_idx] = (0, 0, 0)
                    continue

                # solve sub-questions, do not use function here for performance
                top = dist_tuples[row_idx - 1][col_idx][0] if row_idx > 0 else 0
                left = dist_tuples[row_idx][col_idx - 1][1] if col_idx > 0 else 0
                top_left = dist_tuples[row_idx - 1][col_idx - 1][2] if row_idx > 0 and col_idx > 0 else 0

                max_square_root = min(top, left, top_left) + 1
                if max_square_root > champion_square_root:
                    champion_square_root = max_square_root
                dist_tuples[row_idx][col_idx] = (top + 1, left + 1, max_square_root)
        
        return champion_square_root * champion_square_root


sol = Solution()
test_input = ["0001","1101","1111","0111","0111"]
print sol.maximalSquare(test_input)
