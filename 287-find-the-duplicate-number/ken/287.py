class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = 1
        end = len(nums) - 1

        while start < end:
            m = (end + start) / 2
            cnt = 0

            for num in nums:
                if num <= m:
                    cnt += 1

            if cnt > m:
                end = m
            else:
                start = m + 1

        return start
