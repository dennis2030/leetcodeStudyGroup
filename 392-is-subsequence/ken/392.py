class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == 0:
            return True

        j = 0

        for i in xrange(len(t)):
            if t[i] == s[j]:
                j += 1
                if j == len(s):
                    break

        return j == len(s)
