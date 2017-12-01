class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = 0
        mask = 0
        for idx in xrange(31, -1, -1):
            prefix_set = set()
            mask |= 0x1 << idx
            new_max = max_val | (0x1 << idx)
            for num in nums:
                prefix = num & mask
                prefix_set.add(prefix)
                if (new_max ^ prefix) in prefix_set:
                    max_val |= new_max
                    break

        return max_val
