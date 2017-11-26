class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        best = 0
        for idx, citation in enumerate(citations):
            hIdx = idx + 1
            if hIdx > citation:
                break
            best = hIdx
        return best
