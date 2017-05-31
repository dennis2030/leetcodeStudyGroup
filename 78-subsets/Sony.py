from math import pow

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        all_poss = int(pow(2, nums_len))
        mods_list = [int(pow(2, i)) for i in xrange(nums_len)]
        result_list = [[] for i in xrange(all_poss)]
        print mods_list

        for idx, subset in enumerate(result_list):
            for mod_idx, mod in enumerate(mods_list):
                if idx & mod > 0:
                    subset.append(nums[mod_idx])

        return result_list