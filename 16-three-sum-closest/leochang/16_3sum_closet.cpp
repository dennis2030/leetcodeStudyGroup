class Solution {
public:
	int threeSumClosest(vector<int>& nums, int target) {
		int ans = 0;
		int maxDiff = INT_MAX;
		sort(nums.begin(), nums.end());
		for (int k = 2; k < nums.size(); k++){
			for(int i = 0, j = k - 1; i < j;) {
				int sum = nums[i] + nums[j] + nums[k];
				if (sum < target) {
					if (maxDiff > target - sum) {
						ans = sum;
						maxDiff = target - sum;
					}
					i++;
				} else if (sum > target) {
					if (maxDiff > sum - target) {
						ans = sum;
						maxDiff = sum - target;
					}
					j--;
				} else {
					return target;
				}
			}
		}

		return ans;
	}
};
