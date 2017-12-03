class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def toBin(num):
            return '{:032b}'.format(num)

        def constructTree():
            root = {}
            for num in nums:
                curr = root
                for bit in toBin(num):
                    if bit not in curr:
                        curr[bit] = {}

                    curr = curr[bit]

                    if 'nums' not in curr:
                        curr['nums'] = set([num])
                    else:
                        curr['nums'].add(num)

            return root

        def findBestMatch(num, root):
            fill = (1 << 32) - 1
            complement = fill ^ num
            curr = root
            for bit in toBin(complement):
                if '0' in curr and '1' not in curr:
                    bit = '0'
                if '1' in curr and '0' not in curr:
                    bit = '1'

                curr = curr[bit]

                if len(curr['nums']) == 1:
                    return num ^ list(curr['nums'])[0]

        root = constructTree()

        best = 0
        for num in nums:
            battle = findBestMatch(num, root)
            best = max(battle, best)

        return best
