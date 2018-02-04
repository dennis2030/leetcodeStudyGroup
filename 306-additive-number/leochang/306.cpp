class Solution {
public:
    bool isAdditiveNumber(string num) {
        for (int i = 1; i < num.size(); i++) {
            for (int j = 1; i+j < num.size(); j++) {
                string s1 = num.substr(0,i);
                string s2 = num.substr(i,j);
                if (s1.size() >= 2 && s1[0] == '0') return false;
                if (s2.size() >= 2 && s2[0] == '0') break;
                if (dfs(num.substr(i+j), stol(s1), stol(s2))) {
                    return true;
                }
            }
        }
        
        return false;
    }
    bool dfs(string num, long num1, long num2) {
        if (num.empty()) return true;
        if (num.size() > 1 && num[0] == '0') return false;
        
        string sum = to_string(num1+num2);
        if (string::npos == num.find(sum)) {
            return false;
        }
        
        return dfs(num.substr(sum.size()), num2, stol(sum));
    }
};
