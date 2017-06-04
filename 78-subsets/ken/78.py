class Solution(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		all_subsets = [[]]

		for num in nums:
			new_subsets = [list(subset) + [num] for subset in all_subsets]
			all_subsets.extend(new_subsets)

		return all_subsets
