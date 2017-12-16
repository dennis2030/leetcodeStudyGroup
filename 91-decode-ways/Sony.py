class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp_count = [1]
        prev = ''
        for idx, char in enumerate(s):
            if char == '0':
                if not (prev == '1' or prev == '2'):
                    return 0
                num = dp_count[idx - 1]
            else:
                num = dp_count[idx]
                if prev == '1':
                    num += dp_count[idx - 1]
                elif prev == '2' and int(char) <= 6:
                    num += dp_count[idx - 1]
            dp_count.append(num)
            prev = char

        return dp_count[-1]
