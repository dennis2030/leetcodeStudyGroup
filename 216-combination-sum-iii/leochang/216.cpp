class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> candidates;
        for (int i = 1; i <= 9; i++) {
            candidates.push_back(i);
        }
        
        return combinationSum(candidates, k, n);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int k, int target) {
        vector<vector<int>> ans;
		vector<int> cand;
		sort(candidates.begin(), candidates.end());
        if (candidates.size() == 0) return ans;
        dfs(candidates, target, ans, cand, 0, k);
        return ans;
    }
private:
    void dfs(vector<int>& candidates, int target, vector<vector<int>> &ans, vector<int> &cand, int start, int k) {
        if (0 == k) {
            if (0 == target) {
                ans.push_back(cand);
                return;
            }
            return;
        }
        for (int i = start; i < candidates.size() && candidates[i] <= target; i++) {
            cand.push_back(candidates[i]);
            dfs(candidates, target-candidates[i], ans, cand, i+1, k-1);
            cand.pop_back();
        }
    }
};
