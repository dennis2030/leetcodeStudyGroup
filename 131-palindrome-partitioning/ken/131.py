class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def isPalindrome(s):
            for i in xrange(len(s)):
                if s[i] != s[len(s) - i - 1]:
                    return False

            return True

        ans = []

        for i in xrange(1, len(s) + 1):
            prefix = s[:i]
            suffix = s[i:]
            if not isPalindrome(prefix):
                continue

            if len(suffix) == 0:
                ans.append([prefix])
            else:
                suffix_partitions = self.partition(suffix)
                for partition in suffix_partitions:
                    ans.append([prefix] + partition)

        return ans
