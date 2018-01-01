class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        overlapSum = 0
        for idx in range(len(timeSeries) - 1):
            overlap = timeSeries[idx] + duration - timeSeries[idx + 1]
            if overlap > 0:
                overlapSum += overlap
        return len(timeSeries) * duration - overlapSum
