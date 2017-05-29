class Solution {
public:
	vector<vector<int>> subsets(vector<int>& nums) {
		vector<vector<int>> ret(1, vector<int>());

		sort(nums.begin(), nums.end());
		for (auto num: nums) {
			int size = ret.size();
			for (int i = 0; i < size; i++) {
				ret.push_back(ret[i]);
				ret.back().push_back(num);
			}
		}
		return ret;
	}
};
