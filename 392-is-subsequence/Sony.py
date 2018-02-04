class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import string
        pre_idx = -1
        for i in s:
            pre_idx += 1
            next_idx = string.find(t, i, pre_idx)
            if next_idx == -1:
                return False
            pre_idx = next_idx
        return True
