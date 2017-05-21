class Solution {
public:
	int findMaxForm(vector<string>& strs, int m, int n) {
		vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
		for (auto &str: strs) {
			int zeroNums = 0;
			int oneNums = 0;
			for(auto c: str) {
				if(c == '0') {
					zeroNums++;
				}
			}
			oneNums = str.size() - zeroNums;

			for (int i = m; i >= zeroNums; i--) {
				for (int j = n; j >= oneNums; j--) {
					dp[i][j] = max(dp[i][j], dp[i - zeroNums][j - oneNums] + 1);
				}
			}
		}

		return dp[m][n];
	}
};
