class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> ans;
        int begin = 1, end = n;
        for(int i = k; i > 1; i--) {
            if (i % 2 == 0) {
                ans.push_back(end--);
            } else {
                ans.push_back(begin++);
            }
        }
        for(int i = k-1; i < n; i++) {
            ans.push_back(begin++);
        }
        return ans;
    }
};
