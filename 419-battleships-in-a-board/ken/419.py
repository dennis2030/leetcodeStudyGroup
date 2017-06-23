class Solution(object):
	def countBattleships(self, board):
		"""
		:type board: List[List[str]]
		:rtype: int
		"""

		def isHeadOfBattleship(i, j):
			return (i == 0 or board[i - 1][j] != 'X') and \
				   (j == 0 or board[i][j - 1] != 'X')

		cnt = 0;

		for i in xrange(len(board)):
			for j in xrange(len(board[0])):
				if board[i][j] == 'X' and isHeadOfBattleship(i, j) == True:
					cnt += 1

		return cnt
