class Solution(object):
	def countBits(self, num):
		"""
		:type num: int
		:rtype: List[int]
		"""

		count_bits = [0 for i in xrange(num + 1)]

		for i in xrange(1, num + 1):
			count_bits[i] = count_bits[i / 2] + i % 2

		return count_bits