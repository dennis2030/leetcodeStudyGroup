class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)

        def getRight(rowIdx, colIdx):
            if colIdx >= n - 1:
                return None
            return matrix[rowIdx][colIdx + 1]

        def getDown(rowIdx, colIdx):
            if rowIdx >= n - 1:
                return None
            return matrix[rowIdx + 1][colIdx]

        def setValue(rowIdx, colIdx, value):
            matrix[rowIdx][colIdx] = value

        for idx in range(k - 1):
            colIdx = 0
            rowIdx = 0
            while True:
                right = getRight(rowIdx, colIdx)
                down = getDown(rowIdx, colIdx)
                if right is None and down is None:
                    setValue(rowIdx, colIdx, None)
                    break
                elif right is None:
                    setValue(rowIdx, colIdx, down)
                    rowIdx += 1
                elif down is None:
                    setValue(rowIdx, colIdx, right)
                    colIdx += 1
                elif right < down:
                    setValue(rowIdx, colIdx, right)
                    colIdx += 1
                else:
                    setValue(rowIdx, colIdx, down)
                    rowIdx += 1

        return matrix[0][0]
