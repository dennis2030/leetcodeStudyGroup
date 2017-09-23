class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.length = len(self.nums)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        matched_idx = []
        for i in xrange(self.length):
            if target == self.nums[i]:
                matched_idx.append(i)        
        return matched_idx[random.randint(0, len(matched_idx) - 1)]
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
