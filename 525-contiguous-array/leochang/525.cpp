class Solution {
public:
	int findMaxLength(vector<int>& nums) {
		unordered_map<int,int> map;
		int length = 0;
		int sum = 0;
		map[0] = -1;

		for (int i = 0; i < nums.size(); i++) {
			sum += nums[i] ? 1 : -1;
			if (map.end() == map.find(sum)) {
				map[sum] = i;
			} else {
				length = max(length, i - map[sum]);
			}
		}

		return length;
	}
};
