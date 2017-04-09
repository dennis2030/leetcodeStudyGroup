class Solution {
public:
	vector<string> restoreIpAddresses(string s) {
		vector<string> result;
		int len = s.size();

		for (int i = 1; i < 4; ++i) {
			for (int j = 1; j < 4; ++j) {
				for (int k = 1; k < 4; ++k) {
					if (i + j + k >= len) continue;
					string s1 = s.substr(0, i);
					string s2 = s.substr(i, j);
					string s3 = s.substr(i+j, k);
					string s4 = s.substr(i+j+k, len-i-j-k);
					if (isValid(s1) && isValid(s2) &&
							isValid(s3) && isValid(s4)) {
						string sol = s1 + "."+ s2 + "."+ s3 + "."+ s4;
						result.push_back(sol);
					}
				}
			}
		}
		return result;
	}
	bool isValid(string s){
		if (s.size() > 3 || s.size() == 0 || stoi(s) > 255 || (s.front()=='0' && s.size() > 1)) return false;
		return true;
	}
};
