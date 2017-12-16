class Solution:
    def __init__(self):
        self.dp = {}
        for idx in range(26):
            code = idx + 1
            if code < 10:
                self.dp[str(code)] = 1
            elif code % 10 == 0:
                self.dp[str(code)] = 1
            else:
                self.dp[str(code)] = 2

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s.startswith('0'):
            return 0

        if s in self.dp:
            return self.dp[s]

        ways = 0
        if 1 <= int(s[:1]) <= 9:
            ways += self.numDecodings(s[1:])
        if 10 <= int(s[:2]) <= 26:
            ways += self.numDecodings(s[2:])

        self.dp[s] = ways

        return ways
