class Solution(object):
	def grayCode(self, n):
		"""
		:type n: int
		:rtype: List[int]
		"""

		if n == 0:
			return [0]

		curr_bits = ['0', '1']

		for i in xrange(n - 1):
			prev_bits = curr_bits
			curr_bits = []

			for bit in prev_bits:
				curr_bits.append('0' + bit)

			for bit in reversed(prev_bits):
				curr_bits.append('1' + bit)

		return [int(bit, 2) for bit in curr_bits]
