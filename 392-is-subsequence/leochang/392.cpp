class Solution {
public:
    bool isSubsequence(string s, string t) {
        int s_index = 0;
        if (s.length() == 0) return true;
        if (s.length() != 0 && t.length() == 0) return false;
        
        for (int i = 0; i < t.length(); i++) {
            if (s[s_index] == t[i]) s_index++;
            if (s_index == s.length()) return true;
        }
        
        return false;
    }
};
