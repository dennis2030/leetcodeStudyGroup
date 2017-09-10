class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        import re

        validSubstrs = []

        def getCharCnt(s):
            cnt = {}

            for c in s:
                if c not in cnt:
                    cnt[c] = 0
                cnt[c] += 1

            return cnt

        def getInvalidChars(s):
            invalid = []

            cnt = getCharCnt(s)
            for c in cnt:
                if cnt[c] < k:
                    invalid.append(c)

            return invalid

        def getValidSubStr(s):
            invalidChars = getInvalidChars(s)

            if len(invalidChars) == 0:
                validSubstrs.append(s)
                return

            pattern = '|'.join(invalidChars)
            candidates = re.split(pattern, s)

            for candidate in candidates:
                if candidate:
                    getValidSubStr(candidate)

        getValidSubStr(s)

        maxLen = 0
        for subStr in validSubstrs:
            maxLen = max(maxLen, len(subStr))

        return maxLen

a = Solution()

# print a.longestSubstring('ababbc', 2)

print a.longestSubstring("bbaaacbd", 3)
