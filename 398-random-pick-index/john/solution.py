class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self._nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        indices = []
        for idx, num in enumerate(self._nums):
            if num == target:
                indices.append(idx)
        return random.choice(indices)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
