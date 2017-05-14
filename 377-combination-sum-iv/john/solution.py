class Solution(object):
    def recurse(self, nums, target, prev):
        if target in prev:
            return prev[target]
        if target == 0:
            return 1
        if target < 0:
            return 0

        count = 0
        for num in nums:
            count += self.recurse(nums, target - num, prev)
        prev[target] = count

        return count

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        prev = {}

        return self.recurse(nums, target, prev)
