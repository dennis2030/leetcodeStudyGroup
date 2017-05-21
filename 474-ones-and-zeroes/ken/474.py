class Solution(object):
	def findMaxForm(self, strs, m, n):
		"""
		:type strs: List[str]
		:type m: int
		:type n: int
		:rtype: int
		"""

		memo = [[0] * (n + 1) for i in xrange(m + 1)]

		for s in strs:
			len_0 = s.count('0')
			len_1 = s.count('1')

			for i in xrange(m, len_0 - 1, -1):
				for j in xrange(n, len_1 - 1, -1):
					memo[i][j] = max(memo[i][j], memo[i - len_0][j - len_1] + 1)

		return memo[m][n]
