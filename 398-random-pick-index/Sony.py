class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        target_idxes = []
        for idx, num in enumerate(self.nums):
            if num == target:
                target_idxes.append(idx)
        return random.choice(target_idxes)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)




if __name__ == '__main__':

    nums = [1,2,3,3,3]
    target = 3
    sol = Solution(nums)
    print sol.pick(target)