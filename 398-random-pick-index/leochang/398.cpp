class Solution {
public:
	Solution(vector<int> nums) {
		_nums = nums;
	}

	int pick(int target) {
		int ans = -1;
		int count = 0;
		for (int i = 0 ; i < _nums.size(); i++) {
			if (_nums[i] != target) {
				continue;
			}
			count++;
			if(1 == count || 0 == rand() % count) {
				ans = i;
			}
		}
		return ans;
	}
	vector<int> _nums;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
