class Solution(object):
    def compareNums(self, nums, k):
        lesser_count = 0
        greater_count = 0        
        equal_count = 0
        
        for num in nums:
            if num < k:
                lesser_count += 1
            elif num > k:
                greater_count += 1
            else:
                equal_count += 1
        return lesser_count, greater_count, equal_count
    
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)        
        
        while True:                        
            k = (start + end) / 2
            lesser, greater, equal = self.compareNums(nums, k)            
            if equal > 1:
                return k
            
            if lesser >= k:
                end = k
            else:
                start = k
