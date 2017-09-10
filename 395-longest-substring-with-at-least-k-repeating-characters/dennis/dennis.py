class Solution(object):
    def countCharNum(self, s):
        result_dict = {}
        for c in s:
            if c not in result_dict:
                result_dict[c] = 0
            result_dict[c] += 1
        return result_dict
    
    def getLeastFrequentChar(self, num_dict, k):
        min = k
        min_key = None        
        for key in num_dict:
            if num_dict[key] < min:
                min = num_dict[key]
                min_key = key
        return min_key                
    
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        num_dict = self.countCharNum(s)
        leastFrequentChar = self.getLeastFrequentChar(num_dict, k)
        if leastFrequentChar == None:
            return len(s)
        
        substring_list = s.split(leastFrequentChar)
        return max([self.longestSubstring(substring, k) for substring in substring_list])
