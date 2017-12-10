class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s == '':
            return []

        results = []
        for idx in range(1, len(s) + 1):
            front = s[:idx]
            if not self.isPalindrome(front):
                continue

            tails = self.partition(s[idx:])
            if not tails:
                results.append([front])
            else:
                for tail in tails:
                    results.append([front] + tail)

        return results

    def isPalindrome(self, s):
        return s == ''.join(reversed(s))
