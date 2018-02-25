class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        cnt = 0
        for i in xrange(len(nums) - 2):
            if nums[i] == 0:
                continue

            k = i + 2
            for j in xrange(i + 1, len(nums) - 1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                k -= 1
                cnt += k - j

        return cnt
