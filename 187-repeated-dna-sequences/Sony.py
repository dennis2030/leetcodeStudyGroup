class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        exist_set = set()
        result_set = set()
        str_len = len(s)
        for i in xrange(str_len - 9):
            sub_s = s[i:i + 10]
            if sub_s not in exist_set:
                exist_set.add(sub_s)
            else:
                result_set.add(sub_s)
        return list(result_set)

if __name__ == '__main__':

    sol = Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

    print sol.findRepeatedDnaSequences(s)