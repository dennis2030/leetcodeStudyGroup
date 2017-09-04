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
    intervals.sort((l, r) => ((l.start - r.start) || (r.end - l.end)));
    let count = 0;
    let current = intervals[0];
    for (let i = 1; i < intervals.length; i++) {
        let handle = intervals[i];
        if (handle.start >= current.end) {
            current = handle;
            continue;
        }
        if (handle.end < current.end) current = handle;
        count += 1;
    }
    return count;
};
