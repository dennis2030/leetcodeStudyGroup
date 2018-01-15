class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        results = []

        numIters = (min(m, n) + 1) // 2
        numRows = m
        numCols = n
        for idx in range(numIters):
            rowHeadIdx = idx
            colHeadIdx = idx
            rowTailIdx = idx + numRows - 1
            colTailIdx = idx + numCols - 1

            if numRows == 1 and numCols == 1:
                results.append(matrix[rowHeadIdx][colHeadIdx])
            elif numRows == 1:
                for colIdx in range(colHeadIdx, colTailIdx + 1):
                    results.append(matrix[rowHeadIdx][colIdx])
            elif numCols == 1:
                for rowIdx in range(rowHeadIdx, rowTailIdx + 1):
                    results.append(matrix[rowIdx][colHeadIdx])
            else:
                for colIdx in range(colHeadIdx, colTailIdx):
                    results.append(matrix[rowHeadIdx][colIdx])
                for rowIdx in range(rowHeadIdx, rowTailIdx):
                    results.append(matrix[rowIdx][colTailIdx])
                for colIdx in range(colTailIdx, colHeadIdx, -1):
                    results.append(matrix[rowTailIdx][colIdx])
                for rowIdx in range(rowTailIdx, rowHeadIdx, -1):
                    results.append(matrix[rowIdx][colHeadIdx])

            numRows -= 2
            numCols -= 2

        return results
