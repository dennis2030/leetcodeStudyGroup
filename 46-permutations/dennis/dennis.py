class Solution(object):        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        result = []
        for num in nums:      
            tmp_list = list(nums)
            tmp_list.remove(num)
            remain = self.permute(tmp_list)
            for ele in remain:            
                result.append([num] + ele)  
        return result
        
