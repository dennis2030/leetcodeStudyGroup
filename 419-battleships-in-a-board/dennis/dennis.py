class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        numOfBoats = 0
        
        if len(board) <= 0:
            return numOfBoats
            
        hasShipCols = len(board[0]) * [False]
        hasShipRow = False
        
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] == 'X':
                    if not hasShipCols[j] and not hasShipRow:
                        numOfBoats += 1
                    hasShipCols[j] = True
                    hasShipRow = True
                        
                else:
                    hasShipCols[j] = False
                    hasShipRow = False
            hasShipRow = False
        return numOfBoats
                        
