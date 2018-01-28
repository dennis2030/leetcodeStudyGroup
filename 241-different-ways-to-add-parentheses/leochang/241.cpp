class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> ans;
        for (int i = 0; i < input.size(); i++) {
            if (input[i] == '+' || input[i] == '-' || input[i] == '*') {
                vector<int> ans1 = diffWaysToCompute(input.substr(0, i));
                vector<int> ans2 = diffWaysToCompute(input.substr(i+1));
                for (auto c1 : ans1) {
                    for (auto c2 : ans2) {
                        if (input[i]=='+') ans.push_back(c1+c2);
                        else if (input[i]=='-') ans.push_back(c1-c2);
                        else if (input[i]=='*') ans.push_back(c1*c2);
                    }
                }
            }
        }

        return ans.size() ? ans : vector<int>{stoi(input)};
    }
};
