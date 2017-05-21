class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        
        if len(nums) == 0:
            return result
        
        nums.append(-5566)

        start = nums[0]
        end = nums[0]
        previous = nums[0]
        for i in xrange(1, len(nums)):
            # consecutive
            if (nums[i] - previous) == 1:
                end = nums[i]
                previous = nums[i]
                continue
            
            if start == end:
                result.append(str(start))
            else:
                result.append("{0}->{1}".format(start, end))
                
            start = nums[i]
            end = nums[i]
            
            previous = nums[i]
            
        return result
            
