class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValidBlock(block):
            nums = [elem for elem in block if elem != '.']
            return len(set(nums)) == len(nums)

        def collectSquare(startRowIdx, startColIdx):
            square = []
            for rowIdx in range(startRowIdx, startRowIdx + 3):
                for colIdx in range(startColIdx, startColIdx + 3):
                    square.append(board[rowIdx][colIdx])
            return square

        for row in board:
            if not isValidBlock(row):
                return False

        for colIdx in range(9):
            col = [row[colIdx] for row in board]
            if not isValidBlock(col):
                return False

        for rowIdx in range(0, 9, 3):
            for colIdx in range(0, 9, 3):
                square = collectSquare(rowIdx, colIdx)
                if not isValidBlock(square):
                    return False

        return True
