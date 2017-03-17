class Solution(object):
	def maximalSquare(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return 0

		m = 0
		r = len(matrix)
		c = len(matrix[0])

		for i in xrange(r):
			if "1" in matrix[i]:
				m = 1
				break

		t = [[1 if matrix[i][j] == "1" else 0 for j in xrange(c)] for i in xrange(r)]

		for i in xrange(r - 2, -1, -1):
			for j in xrange(c - 2, -1, -1):
				if matrix[i][j] == "0":
					t[i][j] = 0
					continue

				t[i][j] = min(t[i + 1][j], t[i][j + 1], t[i + 1][j + 1]) + 1
				if t[i][j] > m:
					m = t[i][j]

		return m * m
