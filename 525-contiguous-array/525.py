class Solution(object):
	def findMaxLength(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		first_appear_idx = {}
		last_appear_idx = {}
		first_appear_idx[0] = 0
		last_appear_idx[0] = 0
		s = 0
		for i in xrange(len(nums)):
			if nums[i] == 0:
				s -= 1
			else:
				s += 1

			if s not in first_appear_idx:
				first_appear_idx[s] = i + 1
			last_appear_idx[s] = i + 1

		ret = 0
		for key in first_appear_idx:
			tmp = last_appear_idx[key] - first_appear_idx[key]
			if tmp > ret:
				ret = tmp

		return ret