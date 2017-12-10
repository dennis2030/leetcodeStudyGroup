class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s):
            return s == s[::-1]
        self.result_list = []
        def getPartition(s, prefix_str_list):
            if len(s) == 1:
                candidate = list(prefix_str_list)
                candidate.append(s)
                self.result_list.append(candidate)
                return
            elif len(s) == 0:
                candidate = list(prefix_str_list)
                self.result_list.append(candidate)
                return
            result_list = []
            for i in xrange(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    prefix_str_list.append(s[:i])
                    r = getPartition(s[i:], prefix_str_list)
                    prefix_str_list.pop()
            
        getPartition(s, [])
        return self.result_list
