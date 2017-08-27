class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        def countExactDigits(numOfDigits):
            if numOfDigits == 1:
                return 10

            product = 1
            numOfCandidate = [9] + [9 - i for i in xrange(9)]
            for i in xrange(numOfDigits):
                product *= numOfCandidate[i]

            return product

        if n == 0:
            return 1

        ans = 0
        for i in xrange(n):
            ans += countExactDigits(i + 1)

        return ans
