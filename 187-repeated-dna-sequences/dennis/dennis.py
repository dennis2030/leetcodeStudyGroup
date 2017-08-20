class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        appear_dict = {}
        result_set = set()
        
        
        for i in xrange(len(s)-9):
            substr = s[i:i+10]            
            if substr in appear_dict:
                result_set.add(substr)
            else:
                appear_dict[substr] = 1
                
        return list(result_set)
            
