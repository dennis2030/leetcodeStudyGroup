class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            count = sum([num <= mid for num in nums])

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left
