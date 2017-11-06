class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        counts = {}
        for a in A:
            for b in B:
                addup = a + b
                if addup in counts:
                    counts[addup] += 1
                else:
                    counts[addup] = 1

        result = 0
        for c in C:
            for d in D:
                addup = c + d
                if -addup in counts:
                    result += counts[-addup]

        return result
