class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        return self.searchMatrix2(matrix, target)

    def searchMatrix2(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while True:
            if col < 0 or row >= len(matrix):
                return False

            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1

    def searchMatrix1(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])
        k = min(m, n)

        for i in xrange(k):
            if target == matrix[i][i]:
                return True
            elif target < matrix[i][i]:
                sub1 = []
                for j in xrange(i, m):
                    sub1.append(matrix[j][:i])

                if self.searchMatrix(sub1, target):
                    return True

                sub2 = []
                for j in xrange(i):
                    sub2.append(matrix[j][i:])

                return self.searchMatrix(sub2, target)

        if m == n:
            return False

        sub = []
        if m > n:
            for i in xrange(k, m):
                sub.append(matrix[i][:])
        elif m < n:
            for i in xrange(m):
                sub.append(matrix[i][k:])

        return self.searchMatrix(sub, target)
