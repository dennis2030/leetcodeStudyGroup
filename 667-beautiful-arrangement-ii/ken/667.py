class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        a = []
        for i in xrange(1, n - k):
            a.append(i)

        for i in xrange(k + 1):
            if i % 2 == 0:
                a.append(n - k + i/2)
            else:
                a.append(n - i/2)

        return a
