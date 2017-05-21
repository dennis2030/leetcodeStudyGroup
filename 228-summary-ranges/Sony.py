class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        try:
            result = []
            prev_num = base = nums[0]
            idx = 1
            for idx in xrange(1, len(nums)):
                if nums[idx] - 1 == prev_num:
                    prev_num = nums[idx]
                else:
                    if base == prev_num:
                        result.append(str(base))
                    else:
                        result.append('{0}->{1}'.format(base, prev_num))
                    prev_num = base = nums[idx]
            if base == prev_num:
                result.append(str(base))
            else:
                result.append('{0}->{1}'.format(base, prev_num))
        except:
            pass
        return result
