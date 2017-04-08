class Solution(object):
	def maxRotateFunction(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""

		def F(A, k):
			s = 0

			for i in xrange(len(A)):
				index = (i + k) % len(A)
				s += i * A[index]

			return s

		prev = F(A, 0)
		s = sum(A)
		m = prev

		for i in xrange(1, len(A)):
			cur = prev + s - (len(A) * A[-i])

			if cur > m:
				m = cur
			prev = cur

		return m
