# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        if len(intervals) == 0:
            return 0
        
        # sort by ends
        intervals.sort(key=lambda x: x.end)
        
        result = []
        last_end = intervals[0].start
        for interval in intervals:
            print last_end, interval.start, interval.end
            if interval.start >= last_end:
                print interval.start, interval.end
                result.append(interval)
                last_end = interval.end
        return len(intervals) - len(result)
            
