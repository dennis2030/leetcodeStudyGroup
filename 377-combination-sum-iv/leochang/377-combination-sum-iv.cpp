class Solution {
public:
	int combinationSum4(vector<int>& nums, int target) {
		if (nums.size() == 0 || target <= 0){
			return 0;
		}

		vector<int> vDP(target+1);
		vDP[0] = 1;

		sort (nums.begin(), nums.end());

		for (int i = 1; i <= target; i++) { 
			for (auto num : nums) {
				if (i < num) break;
				vDP[i] += vDP[i - num];
			}
		}
		return vDP[target];
	}
};
