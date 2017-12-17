class Solution {
public:
    int numDecodings(string s) {
        if (0 == s.size() || s[0] == '0') return 0;
        
        vector<int> dp(s.size()+1, 0);
        dp[0] = 1;
        dp[1] = (s[1] != '0') ? 1 : 0;
        
        for (int i = 2; i <= s.size(); i++) {
            if (i < s.size() && s[i] == '0') {
                dp[i] = 0;
            } else if (s[i-2] == '1' || (s[i-2] == '2' && s[i-1] <= '6')) {
                dp[i] = dp[i-1] + dp[i-2];
            } else {
                dp[i] = dp[i-1];
            }
        }
        return dp[s.size()];
    }
};
