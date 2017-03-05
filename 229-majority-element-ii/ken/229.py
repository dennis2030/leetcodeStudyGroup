class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		
		r1 = 0
		r2 = 1
		c1 = 0
		c2 = 0

		for num in nums:
			if num == r1:
				c1 += 1
			elif num == r2:
				c2 += 1
			elif c1 == 0:
				r1 = num
				c1 = 1
			elif c2 == 0:
				r2 = num
				c2 = 1
			else:
				c1 -= 1
				c2 -= 1

		threshold = len(nums) / 3
		res = []

		if nums.count(r1) > threshold:
			res.append(r1)

		if nums.count(r2) > threshold:
			res.append(r2)
		return res

