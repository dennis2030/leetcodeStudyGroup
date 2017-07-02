class Solution(object):
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""

		def validateLine(line):
			cntList = [0 for i in xrange(9)]
			for i in xrange(9):
				if line[i] == '.':
					continue

				cntList[int(line[i]) - 1] += 1

			for cnt in cntList:
				if cnt > 1:
					return False
			return True

		def validateAllRows(board):
			for i in xrange(9):
				if validateLine(board[i]) is False:
					return False
			return True

		def validateAllCols(board):
			for i in xrange(9):
				line = []
				for j in xrange(9):
					line.append(board[j][i])

				if validateLine(line) is False:
					return False
			return True

		def validateAllSubBoxs(board):
			def validateSubBox(row, col):
				line = []

				for i in xrange(3):
					for j in xrange(3):
						line.append(board[row + i][col + j])

				return validateLine(line)

			for i in xrange(3):
				for j in xrange(3):
					if validateSubBox(i * 3, j * 3) is False:
						return False
			return True


		return validateAllRows(board) and \
			   validateAllCols(board) and \
			   validateAllSubBoxs(board)
