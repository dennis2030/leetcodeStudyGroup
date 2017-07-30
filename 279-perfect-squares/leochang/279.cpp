class Solution {
public:
	int numSquares(int n) {
		vector<int> dp (n+1, n);
		dp[0] = 0;
		for (int i = 1; i <= n; i++){
			for (int j = 1; j * j <= i; j++) {
				dp[i] = min(dp[i-j*j] + 1, dp[i]);
			}
		}
		return dp[n];
	}
};
