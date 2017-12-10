class Solution(object):
    def isPalindrone(self, s):
        return 0 == sum(1 for i in xrange(len(s)) if s[i] != s[-1-i])
    
    def recursiveFindPalindrone(self, s):
        if s in self.partition_dict:
            return self.partition_dict[s]
                     
        ans = []
        if self.isPalindrone(s):
            ans.append([s])
        
        for i in xrange(1, len(s)):            
            first_part = s[:i]            
            if not self.isPalindrone(first_part):
                continue            
            combinations = self.recursiveFindPalindrone(s[i:])                        
            for comb in combinations:
                result = [first_part]
                for part in comb:
                    result.append(part)
                ans.append(result)            
        self.partition_dict[s] = ans
        
        return ans
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.partition_dict = {}
        
        return self.recursiveFindPalindrone(s)
