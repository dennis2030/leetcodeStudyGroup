class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)

        def countSmallerRow(target, row):
            for idx, elem in enumerate(row):
                if target < elem:
                    return idx
            return n

        def countSmaller(target):
            count = 0
            for row in matrix:
                count += countSmallerRow(target, row)
            return count

        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = int((left + right) / 2)
            count = countSmaller(mid)
            print mid, count
            if count < k:
                left = mid + 1
            else:
                right = mid

        return left
