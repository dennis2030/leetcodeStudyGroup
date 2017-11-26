class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(key=lambda x: -x)
        for i in xrange(len(citations)):
            if i >= citations[i]:
                return i
            elif i + 1 == citations[i]:
                return i + 1
        
        return len(citations) if len(citations) > 0 else 0
