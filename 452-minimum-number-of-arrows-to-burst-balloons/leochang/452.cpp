class Solution {
public:
	int findMinArrowShots(vector<pair<int, int>>& points) {
		int count = 0;
		int arrow = INT_MIN;

		sort(points.begin(), points.end(), compare);

		for (int i = 0; i < points.size(); i++) {
			if (arrow != INT_MIN && points[i].first <= arrow) {
				continue;
			}
			arrow = points[i].second;
			count++;
		}

		return count;
	}
	static bool compare (pair<int, int> &i, pair<int, int> &j) {
		return (i.second < j.second);
	}
};
