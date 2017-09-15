# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda interval: interval.end)

        num_erase = 0
        smallest_idx = 0
        for idx in xrange(1, len(intervals)):
            if intervals[idx].start < intervals[smallest_idx].end:
                num_erase += 1
            else:
                smallest_idx = idx

        return num_erase


if __name__ == '__main__':

    sol = Solution()

    L = [[1,100],[11,22],[1,11],[2,12]]
    intervals = []
    for l in L:
        intervals.append(Interval(l[0], l[1]))
    print sol.eraseOverlapIntervals(intervals)