class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len = len(s)
        if s_len == 0:
            return True
        
        curr_s_idx = 0
        curr_s = s[curr_s_idx]
        
        
        for c in t:
            if c == curr_s:
                curr_s_idx += 1
                if curr_s_idx == s_len:
                    return True
                curr_s = s[curr_s_idx]
        return False
