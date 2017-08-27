class Solution {
public:
	vector<string> findRepeatedDnaSequences(string s) {
		vector<string> ans;
		unordered_map<string, int> m;
		for (int i = 0; i + 9 < s.size(); i++){
			string strTen = s.substr(i, 10);
			if (m[strTen] == 1) {
				ans.push_back(strTen);
			}
			m[strTen]++;
		}
		return ans;
	}
};
