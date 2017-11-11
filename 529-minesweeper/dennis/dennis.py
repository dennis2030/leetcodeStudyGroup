class Solution(object):    
    def isPosValid(self, board, r, c):
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):            
            return False
        return True
    
    def isMine(self, board, r, c):
        if self.isPosValid(board, r, c) and board[r][c] == 'M':
            return True
        return False
        
    def checkNeighborMine(self, board, r, c):
        total_mine = 0
        for tmp_r in [i-1 for i in xrange(3)]:
            for tmp_c in [j-1 for j in xrange(3)]:                
                if self.isMine(board, r + tmp_r, c + tmp_c):
                    total_mine += 1
        return total_mine
            
        
    def updateEmptyBlock(self, board, r, c):
        if not self.isPosValid(board, r, c):
            return
        
        if board[r][c] != 'E':
            return
        
        # update self
        neighbor_mine = self.checkNeighborMine(board, r, c)        
        if neighbor_mine > 0:
            board[r][c] = str(neighbor_mine)            
            return
        
        board[r][c] = 'B'
                
        for tmp_r in [i-1 for i in xrange(3)]:
            for tmp_c in [j-1 for j in xrange(3)]:
                self.updateEmptyBlock(board, r + tmp_r, c + tmp_c)        
        
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        click_r = click[0]
        click_c = click[1]
        
        # if click on mine
        if board[click_r][click_c] == 'M':
            board[click_r][click_c] = 'X'
            return board
        
        # click on empty block
        self.updateEmptyBlock(board, click_r, click_c)
        
        return board
