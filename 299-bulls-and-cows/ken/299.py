class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        A = 0
        B = 0
        letterCnt = {}

        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if secret[i] not in letterCnt:
                    letterCnt[secret[i]] = 0
                elif letterCnt[secret[i]] < 0:
                    B += 1
                letterCnt[secret[i]] += 1

                if guess[i] not in letterCnt:
                    letterCnt[guess[i]] = 0
                elif letterCnt[guess[i]] > 0:
                    B += 1
                letterCnt[guess[i]] -= 1

        return "%dA%dB" % (A, B)
