class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        block_rec = [set() for i in xrange(9)]
        row_rec = [set() for i in xrange(9)]
        column_rec = [set() for i in xrange(9)]

        for i in xrange(9):
        	for j in xrange(9):
        		elem = board[i][j]
        		if elem != '.':
        			if elem in block_rec[i / 3 * 3 + j / 3] or elem in row_rec[i] or elem in column_rec[j]:
        				print block_rec
        				print row_rec
        				print column_rec
        				print i,j, elem
        				return False
        			block_rec[i / 3 * 3 + j / 3].add(elem)
        			row_rec[i].add(elem)
        			column_rec[j].add(elem)
        return True



if __name__ == '__main__':

    sol = Solution()
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]

    print sol.isValidSudoku(board)