class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        def canMutate(src, dst):
            return (1 == sum([0 if src[i] == dst[i] else 1 for i in xrange(len(src))]))

        currGeneration = set([start])
        bank = set(bank)
        length = 0

        while currGeneration:
            nextGeneration = set()
            length += 1
            for src in currGeneration:
                for dst in bank:
                    if canMutate(src, dst):
                        if dst == end:
                            return length

                        nextGeneration.add(dst)
                bank -= nextGeneration

            currGeneration = nextGeneration

        return -1
