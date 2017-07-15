class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """

        def findSubStrLenAtIdx(s, idx):
            prev_c = s[idx]
            cnt = 1

            for i in xrange(idx + 1, len(s)):
                curr_c = s[i]

                if (ord(curr_c) - ord(prev_c) != 1) and \
                   not (prev_c == 'z' and curr_c == 'a'):
                    break

                prev_c = curr_c
                cnt += 1

            return cnt

        maxStrLenList = [0 for i in xrange(ord('a'), ord('z') + 1)]
        i = 0
        while i < len(p):
            substrLen = findSubStrLenAtIdx(p, i)

            for j in xrange(substrLen):
                idx = ord(p[i + j]) - ord('a')
                newLen = substrLen - j
                maxStrLenList[idx] = max(newLen, maxStrLenList[idx])

            i += substrLen

        return sum(maxStrLenList)
