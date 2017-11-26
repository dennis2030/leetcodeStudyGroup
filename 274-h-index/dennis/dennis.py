class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """                
        citations.sort()
        h_index = 0
        
        for i in xrange(len(citations)):            
            if citations[i] >= len(citations) - i:
                h_index = len(citations) - i
                break
            
        return h_index
