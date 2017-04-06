class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum_all = sum(A)
        N = len(A)

        F_0 = sum([x[0]*x[1] for x in zip(A, range(N))])

        champion = F_0
        previous = F_0
        for i in xrange(1, N):
            current = previous - A[N-i]*(N) + sum_all
            if current > champion:
                champion = current
            previous = current
        return champion
