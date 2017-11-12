class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
            return [list(nums)]

        ans = []

        for i in xrange(len(nums)):
            n = nums[i]
            del nums[i]

            tmp = self.permute(nums)

            for t in tmp:
                t.insert(0, n)
                ans.append(t)

            nums.insert(i, n)

        return ans
