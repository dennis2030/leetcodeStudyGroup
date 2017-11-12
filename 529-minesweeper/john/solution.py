class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def getCell(row, col):
            if row < 0 or col < 0:
                return None
            if row >= len(board) or col >= len(board[0]):
                return None
            return board[row][col]

        def setCell(row, col, val):
            board[row][col] = val

        def offsetClick(rowOffset, colOffset):
            row = click[0]
            col = click[1]
            return [row + rowOffset, col + colOffset]

        if getCell(*click) == 'M':
            setCell(*click, 'X')
            return board

        if getCell(*click) != 'E':
            return board

        numMine = 0
        for rowOffset in [-1, 0, 1]:
            for colOffset in [-1, 0, 1]:
                newClick = offsetClick(rowOffset, colOffset)
                if getCell(*newClick) == 'M':
                    numMine += 1

        if numMine > 0:
            setCell(*click, str(numMine))
            return board

        setCell(*click, 'B')

        for rowOffset in [-1, 0, 1]:
            for colOffset in [-1, 0, 1]:
                newClick = offsetClick(rowOffset, colOffset)
                self.updateBoard(board, newClick)

        return board
