class Solution(object):
    def __init__(self):
        self.dp = {}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s in self.dp:
            return self.dp[s]
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        n = 0
        if len(s[:2]) == 2 and s[:2] > '0' and s[:2] <= '26':
            if (len(s[2:]) == 0):
                n += 1
            else:
                n += self.numDecodings(s[2:])

        n += self.numDecodings(s[1:])

        if s not in self.dp:
            self.dp[s] = n

        return n
