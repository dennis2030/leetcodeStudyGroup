class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        cnt = 0
        p = [a + b for a in A for b in B]
        q = [c + d for c in C for d in D]
        p.sort()
        q.sort(reverse=True)
        N = len(p)

        i = 0
        j = 0
        while i < N and j < N:
            s = p[i] + q[j]

            if s > 0:
                j += 1
            elif s < 0:
                i += 1
            else:
                dupCnt1 = 1
                dupCnt2 = 1
                while i + dupCnt1 < N and p[i] == p[i + dupCnt1]:
                    dupCnt1 += 1
                while j + dupCnt2 < N and q[j] == q[j + dupCnt2]:
                    dupCnt2 += 1

                cnt += (dupCnt1 * dupCnt2)
                i += dupCnt1
                j += dupCnt2

        return cnt
