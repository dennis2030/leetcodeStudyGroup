class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        repeated = []
        cnt = {}

        for i in xrange(len(s) - 9):
            tmp = s[i:i + 10]
            if tmp not in cnt:
                cnt[tmp] = 0
            cnt[tmp] += 1

        for k in cnt:
            if cnt[k] > 1:
                repeated.append(k)

        return repeated
