class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        # TLE: n = 6052
        def DP(n):
            dp = [None for i in xrange(n + 1)]
            dp[0] = 0

            for i in xrange(1, n + 1):
                j = 1
                while True:
                    if j * j > i:
                        break

                    if dp[i] == None:
                        dp[i] = dp[i - j * j] + 1
                    dp[i] = min(dp[i], dp[i - j * j] + 1)

                    j += 1

            return dp[n]

        # TLE: n = 1535, if using list instead of set
        def BFS(n):
            perfectNums = []

            i = 1
            while i * i <= n:
                perfectNums.append(i * i)
                i += 1

            curNodes = {n}
            depth = 1
            while curNodes:
                nextNodes = set()

                for curNode in curNodes:
                    for perfectNum in perfectNums:
                        nextNode = curNode - perfectNum
                        if nextNode == 0:
                            return depth
                        if nextNode > 0:
                            nextNodes.add(nextNode)

                depth += 1
                curNodes = nextNodes

            return depth

        return BFS(n)
