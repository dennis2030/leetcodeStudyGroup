class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp_dict = {0: 1}
        nums_len = len(nums)
        nums.sort()
        try:
            dp_dict[nums[0]] = 1
            for i in xrange(nums[0] + 1, target + 1):
                dp_dict[i] = 0
                for j in xrange(nums_len):
                    difference = i - nums[j]
                    if difference in dp_dict:
                        dp_dict[i] += dp_dict[difference]
            return dp_dict[target]
        except IndexError:
            #length of nums is zero
            return 0
        except KeyError:
            #no combination found
            return 0
