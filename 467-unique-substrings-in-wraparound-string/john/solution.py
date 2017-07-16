class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        def isContinuous(a, b):
            return (a + 1) % 26 == b

        lengths = [0] * 26
        nums = [ord(c) - ord('a') for c in p]

        for idx in range(len(nums)):
            if idx == 0:
                length = 1
            elif isContinuous(nums[idx - 1], nums[idx]):
                length += 1
            else:
                length = 1

            last = nums[idx]
            lengths[last] = max(lengths[last], length)

        return sum(lengths)
