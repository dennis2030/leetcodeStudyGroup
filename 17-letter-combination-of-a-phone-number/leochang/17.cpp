class Solution {
public:
	vector<string> letterCombinations(string digits) {
		vector<string> ret;
		string strMaps[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

		if (0 == digits.size()) {
			return ret;
		}

		ret.push_back("");

		for(int i = 0; i < digits.size(); i++) {
			int num = digits[i] - '0';
			string strChars = strMaps[num];
			vector<string> tmp;
			for (int j = 0; j < ret.size(); j++) {
				for (int k = 0; k < strChars.size(); k++) {
					tmp.push_back(ret[j] + strChars[k]);
				}
			}
			ret = tmp;
		}
		return ret;
	}
};
