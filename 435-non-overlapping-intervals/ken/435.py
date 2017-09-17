# Definition for an interval.
#class Interval(object):
#    def __init__(self, s=0, e=0):
#        self.start = s
#        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        length = len(intervals)

        if length == 0:
            return 0

        cnt = 0
        intervals.sort(key=lambda x : x.start)
        end = intervals[0].end

        for i in xrange(1, length):
            interval = intervals[i]

            if interval.start >= end:
                end = interval.end
            else:
                cnt += 1
                end = min(end, interval.end)

        return cnt
