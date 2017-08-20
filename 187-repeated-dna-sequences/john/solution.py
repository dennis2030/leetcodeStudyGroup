class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        seen = set()
        repeat = set()
        curr = s[:10]
        seen.add(curr)
        for idx in range(10, len(s)):
            curr = curr[1:] + s[idx]
            if curr in seen:
                repeat.add(curr)
            seen.add(curr)
        return list(repeat)
