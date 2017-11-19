class Solution {
public:
    string replaceWords(vector<string>& dict, string sentence) {
        string ans;
        istringstream iss(sentence);
        
        for(string s; iss >> s;) {
            string replaceStr = replace(dict, s);
            ans = ans + replaceStr + " ";
        }
        
        return ans.substr(0, ans.size()-1);
    }
    string replace(vector<string>& dict, string s) {
        string ret = s;
        
        for (auto dictStr : dict) {
            if (0 == s.find(dictStr) && dictStr.size() < ret.size()) {
                ret = dictStr;
            }
        }
        
        return ret;
    }
};
