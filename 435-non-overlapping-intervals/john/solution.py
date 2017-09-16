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
        items = [{'erased': False, 'interval': interval} for interval in intervals]
        items.sort(key=lambda item: item['interval'].start)

        for idx, item in enumerate(items):
            if item['erased']:
                continue
            for jtem in items[idx + 1:]:
                if item['interval'].end <= jtem['interval'].start:
                    break
                if item['interval'].end <= jtem['interval'].end:
                    jtem['erased'] = True
                else:
                    item['erased'] = True
                    break

        return sum([item['erased'] for item in items])
