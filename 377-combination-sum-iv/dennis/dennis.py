class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import collections
        result_dict = collections.defaultdict(int)
        
        for num in nums:
            result_dict[num] += 1
        
        for i in xrange(target):
            for num in nums:
                result_dict[i + num] += result_dict[i]
        return result_dict[target]
