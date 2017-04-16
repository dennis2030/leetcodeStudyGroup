class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        count = 0
        
        count_idx_dict = {0: -1}
        
        for i in xrange(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
                
            if count in count_idx_dict:
                max_length = max(max_length, i - count_idx_dict[count])
            else:
                count_idx_dict[count] = i
                
        return max_length
