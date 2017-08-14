/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    if (intervals.length === 0) return 0;
    intervals.sort((a, b) => {
        return a.start < b.start ? -1 : a.start > b.start ? 1 : a.end < b.end ? -1 : 1;
    });
    var x = intervals[0].end, c = 0;
    for (var i=1; i<intervals.length; ++i) {
        if (intervals[i].start < x) {
            ++c;
            x = Math.min(x, intervals[i].end);
        }
        else x = intervals[i].end;
    }
    return c;
};
