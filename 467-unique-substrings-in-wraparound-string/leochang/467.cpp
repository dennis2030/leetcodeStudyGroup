class Solution {
public:
	int findSubstringInWraproundString(string p) {
		if (p.size() == 0) return 0;

		int sum = 0, max_len = 1;
		vector<int> dp(26, 0);

		dp[p[0] - 'a'] = max_len;

		for (int i = 1; i < p.size(); i++) {
			int tmp = p[i] - 'a';
			if (((p[i-1] - 'a')  + 1) % 26 == tmp) {
				max_len++;
			} else {
				max_len = 1;
			}
			dp[tmp] = max(max_len, dp[tmp]);
		}

		for (int i = 0; i < 26; i++) {
			sum += dp[i];
		}

		return sum;
	}
};
