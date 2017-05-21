class Solution {
public:
	vector<string> summaryRanges(vector<int>& nums) {
		vector<string> ret;
		bool inRange = false;
		int startNum = 0;
		int lastNum = 0;
		string sRet;
		int sizeNums = nums.size();

		if (0 == sizeNums){
			return ret;
		}

		startNum = nums[0];
		lastNum = nums[0];
		sRet = to_string(startNum);

		for (int i = 1; i < sizeNums; i++) {
			if (nums[i] != lastNum + 1) {
				if (startNum != lastNum) {
					sRet = sRet + "->" + to_string(lastNum);
				}
				ret.push_back(sRet);
				startNum = nums[i];
				lastNum = nums[i];
				sRet = to_string(startNum);
			} else {
				lastNum = nums[i];
			}
		}

		if (startNum != lastNum) {
			sRet = sRet + "->" + to_string(lastNum);
		}
		ret.push_back(sRet);

		return ret;
	}
};
