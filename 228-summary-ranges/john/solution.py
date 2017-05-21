class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []

        for num in nums:
            if not ranges or num > ranges[-1][1] + 1:
                ranges.append([num, num])
            else:
                ranges[-1][1] = num

        result = []
        for range in ranges:
            if range[0] == range[1]:
                result.append('{}'.format(range[0]))
            else:
                result.append('{}->{}'.format(range[0], range[1]))
        return result
