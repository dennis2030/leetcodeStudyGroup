class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        def numForSlice(start, end):
            n = end - start - 1
            return n*(n+1)/2

        if len(A) < 3:
            return 0

        ans = 0
        diff = A[1] - A[0]
        start = 0

        for i in xrange(1, len(A) - 1):
            if i == len(A) - 2:
                end = i
                if diff == A[i + 1] - A[i]:
                    end += 1

                ans += numForSlice(start, end)
                break

            if (A[i + 1] - A[i]) != diff:
                ans += numForSlice(start, i)

                diff = A[i + 1] - A[i]
                start = i

        return ans
