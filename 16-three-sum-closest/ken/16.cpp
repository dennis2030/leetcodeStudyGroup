class Solution {
public:
	int threeSumClosest(vector<int>& nums, int target) {
		int ans = nums[0] + nums[1] + nums[2];
		int n = nums.size();

		sort(nums.begin(), nums.end());

		for (int i = 0; i < n - 2; i++) {
			int j = i + 1;
			int k = n - 1;

			while (j < k) {
				int sum = nums[i] + nums[j] + nums[k];

				if (abs(target - sum) < abs(target - ans)) {
					ans = sum;
					if (ans == target) {
						return ans;
					}
				}

				if (sum < target) {
					j++;
				} else {
					k--;
				}
			}
		}


		return ans;
	}
};
