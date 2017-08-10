class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        dp = [1, 10, 91]
        i = 3
        base = 9 * math.factorial(9)
        while i <= n and i <= 10:
            dp.append(dp[i - 1] + base / math.factorial(9 - i + 1))
            i += 1
        if n > 10:
            return dp[10]
        else:
            return dp[n]
if __name__ == '__main__':

    sol = Solution()
    n = "10"

    print sol.countNumbersWithUniqueDigits(n)