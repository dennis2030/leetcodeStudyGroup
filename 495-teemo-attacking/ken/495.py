class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        if len(timeSeries) == 0:
            return 0

        ans = 0
        start = timeSeries[0]
        for t in timeSeries:
            ans += min(t - start, duration)
            start = t

        ans += duration

        return ans
