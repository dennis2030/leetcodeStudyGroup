class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

		sorted_nums = list(nums)
		sorted_nums.sort()

		med = len(nums) / 2
		if len(nums) % 2 == 0:
			med -= 1
		small = sorted_nums[:med + 1]
		large = sorted_nums[med + 1:]

		n = len(nums)

		if n % 2 == 0:
			for i in xrange(len(small)):
				nums[i * 2] = large[i]
				nums[i * 2 + 1] = small[i]
		else:
			for i in xrange(len(small)):
				nums[i * 2] = small[i]
				if i < len(large):
					nums[i * 2 + 1] = large[i]

		nums.reverse()
