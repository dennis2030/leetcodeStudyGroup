class Solution {
public:
	int longestSubstring(string s, int k) {
		vector<int> count(26, 0);
		for(char c : s) count[c-'a']++;
		for(int i = 0; i < s.length(); i++) {
			if (count[s[i] - 'a'] < k && count[s[i] - 'a'] > 0) {
				int ans = 0;
				stringstream ss(s);
				string substr;
				while(getline(ss, substr, s[i])) {
					ans = max(ans, longestSubstring(substr, k));
				}
				return ans;
			}
		}
		return s.length();
	}
};
