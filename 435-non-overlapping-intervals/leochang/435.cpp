/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
	int eraseOverlapIntervals(vector<Interval>& intervals) {
		if (0 == intervals.size()) return 0;
		sort(intervals.begin(), intervals.end(), comp);
		int count = 1;
		int end = intervals[0].end;
		for (int i = 1; i < intervals.size(); i++) {
			if (intervals[i].start >= end) {
				end = intervals[i].end;
				count++;
			}
		}
		return intervals.size() - count;
	}
	static bool comp(Interval& p1, Interval& p2) {
		return p1.end < p2.end;
	}
};
