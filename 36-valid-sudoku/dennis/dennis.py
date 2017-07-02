class Solution(object):
    def is_valid(self, l):        
        bit_map = 0
        
        for ele in l:            
            if ele == '.':
                continue            
            if bit_map & (1 << int(ele)) > 0:
                return False
            else:
                bit_map += (1 << int(ele))
        return True
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # validate rows
        for row in board:
            if not self.is_valid(row):
                return False
        # validate cols
        for i in xrange(len(board)):
            if not self.is_valid([row[i] for row in board]):
                return False
            
        # validate grid
        for i in xrange(3):
            for j in xrange(3):
                if not self.is_valid(sum([row[j*3:j*3+3] for row in board[i*3:i*3+3]], [])):                
                    return False
        
        return True
