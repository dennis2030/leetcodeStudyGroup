class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = sorted(nums, key = lambda x: -x)
        nums_len = len(nums)
        nums = 0
        for i in xrange(0, nums_len - 2):
            j = i + 1
            k = nums_len - 1
            while j != k:
                if new_nums[j] + new_nums[k] > new_nums[i]:
                    nums += k - j
                    j += 1
                else:
                    k -= 1
                    
        return nums
