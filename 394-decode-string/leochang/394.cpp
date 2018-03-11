class Solution {
public:
    string decodeString(string s) {
        int curr = 0;
        return dfs(s, curr);
    }
    string dfs(string& s, int& curr) {
        string ret = "";
        int num = 0;
        
        while (curr < s.size()) {
            if (isdigit(s[curr])) {
                num = num*10 + (s[curr] - '0');
            } else if (s[curr] == '[') {
                string tmp = dfs(s, ++curr);
                for(; num > 0; num--) ret += tmp;
            } else if (s[curr] == ']') {
                break;
            } else {
                ret += s[curr];
            }
            curr++;
        }
        
        return ret;
    }
};
