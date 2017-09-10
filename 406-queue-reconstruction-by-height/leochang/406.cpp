class Solution {
public:
	vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
		sort(people.begin(), people.end(), comp);
		vector<pair<int, int>> ret;
		for (auto &p: people) {
			ret.insert(ret.begin() + p.second, p);
		}
		return ret;
	}
	static bool comp(pair<int, int>& p1, pair<int, int>& p2) {
		if (p1.first != p2.first) {
			return p1.first > p2.first;
		} else {
			return p1.second < p2.second;
		}
	}
};
