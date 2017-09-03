class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        dp = {}

        def toKey(depth, remains):
            s = '%d' % depth
            for r in remains:
                s += '_%d' % r

            return s

        def is_beautiful(a, b):
            if a % b == 0 or b % a == 0:
                return True
            return False

        def dfs(depth, candidates):
            cnt = 0
            for i in xrange(len(candidates)):
                if not is_beautiful(depth, candidates[i]):
                    continue

                remains = list(candidates)
                remains.pop(i)

                if len(remains) == 0:
                    cnt += 1
                else:
                    k = toKey(depth + 1, remains)
                    if k not in dp:
                        c = dfs(depth + 1, remains)
                        dp[k] = c

                    cnt += dp[k]

            return cnt

        cnt = dfs(1, [i for i in xrange(1, N + 1)])
        return cnt
