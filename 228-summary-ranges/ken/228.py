class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""

		ret = []

		start = None
		prev = None
		for i in xrange(len(nums)):
			if start is None:
				start = nums[i]

			if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
				if start == nums[i]:
					ret.append("%d" % (start))
				else:
					ret.append("%d->%d" % (start, nums[i]))
				start = None

		return ret

a = Solution()

print a.summaryRanges([0,1,2,4,5,7])
print a.summaryRanges([7,8,10])