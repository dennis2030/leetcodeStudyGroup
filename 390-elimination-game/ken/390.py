class Solution(object):
	def lastRemaining(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		start = 1
		end = n
		step = 1

		while n > 1:
			end = start + (n - 1) * step
			start = end - (n % 2) * step
			n /= 2
			step *= -2

		return start