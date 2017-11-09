class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        permute_results = []
        if nums_len == 0:
            return []
        elif nums_len == 1:
            return [nums]
        num = nums.pop()
        sub_permutes = self.permute(nums)
        for one_permute in sub_permutes:
            new_permute = [num] + list(one_permute)
            permute_results.append(new_permute)
            for i in xrange(1, nums_len):
                new_permute = list(new_permute)
                tmp_num = new_permute[i - 1]
                new_permute[i - 1] = new_permute[i]
                new_permute[i] = tmp_num
                permute_results.append(new_permute)

        return permute_results
        
sol = Solution()
nums = [1, 2, 3]
print sol.permute(nums)
