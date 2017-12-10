class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ret;
        dfs(ret, vector<string>(), s, 0);
        return ret;
    }
    void dfs(vector<vector<string>> &ret, vector<string> candidate, string s, int start) {
        if (start == s.size()) {
            ret.push_back(candidate);
            return;
        }
        for (int i = 1; start+i <= s.size(); i++) {
            if (isPalindrome(s.substr(start, i))) {
                candidate.push_back(s.substr(start, i));
                dfs(ret, candidate, s, start+i);
                candidate.pop_back();
            }
        }
    }
    bool isPalindrome(string s) {
        if (s.size() == 1) {
            return true;
        }
        for (int start = 0, end = s.size()-1; start < end; start++, end--) {
            if (s[start] != s[end]) {
                return false;
            }
        }
        return true;
    }
};
