class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxXOR = 0

        for bit in range(32)[::-1]:
            s = set()
            candidate = maxXOR | (0x01 << bit)

            for n in nums:
                p = n & candidate

                q = candidate ^ p
                if q in s:
                    maxXOR = candidate
                    break

                s.add(p)

        return maxXOR
