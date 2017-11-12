class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        height = len(board)
        width = len(board[0])
        genNeighbors = lambda click : [(row1, col1) for row1 in range(click[0]-1, click[0]+2) \
                                                    for col1 in range(click[1]-1, click[1]+2) \
                                                    if (row1 >= 0 and row1 < height and \
                                                        col1 >= 0 and col1 < width)]

        def getNewCell(board, neightbors):
            mineCnt = 0
            for neighbor in neightbors:
                if board[neighbor[0]][neighbor[1]] == 'M':
                    mineCnt += 1

            return 'B' if (mineCnt == 0) else str(mineCnt)

        def rec(board, click):
            if board[click[0]][click[1]] != 'E':
                return

            neightbors = genNeighbors(click)

            board[click[0]][click[1]] = getNewCell(board, neightbors)
            if board[click[0]][click[1]] != 'B':
                return

            for neighbor in neightbors:
                rec(board, neighbor)

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        rec(board, click)

        return board
