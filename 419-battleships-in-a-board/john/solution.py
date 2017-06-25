class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for idx, row in enumerate(board):
            for jdx, elem in enumerate(row):
                if elem == '.':
                    continue
                if idx > 0 and board[idx - 1][jdx] == 'X':
                    continue
                if jdx > 0 and row[jdx - 1] == 'X':
                    continue
                cnt += 1
        return cnt
