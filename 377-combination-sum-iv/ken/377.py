class Solution(object):
	def combinationSum4(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""

		m = {}
		m[0] = 1

		def foo(target):
			if target in m:
				return m[target]
			if target < 0:
				return 0

			ret = 0
			for num in nums:
				ret += foo(target - num)
			m[target] = ret

			return ret

		# return foo(target)

		l = [0 for i in xrange(target+1)]
		l[0] = 1

		def bar(target):
			for i in xrange(target + 1):
				for j in xrange(len(nums)):
					if i - nums[j] >= 0:
						l[i] += l[i - nums[j]]
			return l[target]

		return bar(target)
