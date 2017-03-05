#!/usr/bin/env python2

class Solution(object):
    def twoSum(self, nums, target):
        sum = nums[0] + nums[-1]
        if sum == target or len(nums) == 2:
            return sum
        elif sum > target:
            result = self.twoSum(nums[:-1], target)
        else:
            result = self.twoSum(nums[1:], target)
        return result if abs(sum-target) > abs(result-target) else sum
    
    def threeSumClosest(self, nums, target):
        nums.sort()
        for i in xrange( len(nums)-2 ):
            target_i = target - nums[i]
            tmp_3_sum = nums[i] + self.twoSum(nums[i+1:], target_i)
            if (i == 0) or (abs(target - tmp_3_sum) < abs(target - winner)):
                winner = tmp_3_sum
            if winner == target:
                break
        return winner



sol = Solution()
nums = [0,2,1,-3]
print sol.threeSumClosest(nums, 1)
