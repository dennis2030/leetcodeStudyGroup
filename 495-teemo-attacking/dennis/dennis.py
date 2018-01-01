class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        if len(timeSeries) == 0:
            return 0
        
        diffs = [timeSeries[i] - timeSeries[i-1] for i in xrange(1, len(timeSeries))]
        
        ans = 0
        for diff in diffs:
            if diff < duration:
                ans += diff
            else:
                ans += duration
        # add the last part
        ans += duration
        return ans
