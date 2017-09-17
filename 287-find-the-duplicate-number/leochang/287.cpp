class Solution {
public:
	int findDuplicate(vector<int>& nums) {
		int low = 1, high = nums.size() - 1;
		while (low < high) {
			int mid = (low + high) / 2, count = 0;
			for (auto num : nums) {
				if (num <= mid) {
					count++;
				}
			}
			if (count > mid) {
				high = mid;
			} else {
				low = mid + 1;
			}
		}
		return low;
	}
};
