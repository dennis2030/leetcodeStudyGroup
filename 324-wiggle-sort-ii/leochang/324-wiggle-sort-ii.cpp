class Solution {
public:
	void wiggleSort(vector<int>& nums) {
		vector<int> sortArray(nums);
		sort(sortArray.begin(), sortArray.end());
		int begin = 0;
		int end;
		if (nums.size() % 2 == 0) {
			end = nums.size() / 2;
		} else {
			end = nums.size() / 2 + 1;
		}
		for(int i = nums.size() - 1; i >= 0; --i) {
			if (i % 2 == 0) {
				nums[i] = sortArray[begin];
				begin++;
			} else {
				nums[i] = sortArray[end];
				end++;
			}
		}
	}
};
