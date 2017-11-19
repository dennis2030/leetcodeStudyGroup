class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = range(1, n - k)
        for i in xrange(k+1):            
            result.append(n - k + int(i/2) if (i %2 == 0) else n - int(i/2))
        return result
