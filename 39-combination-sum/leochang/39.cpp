class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
		vector<int> cand;
		sort(candidates.begin(), candidates.end());
        if (candidates.size() == 0) return ans;
        dfs(candidates, target, ans, cand, 0);
        return ans;
    }
private:
    void dfs(vector<int>& candidates, int target, vector<vector<int>> &ans, vector<int> &cand, int start) {
        if (0 == target) {
            ans.push_back(cand);
            return;
        }
        for (int i = start; i < candidates.size() && candidates[i] <= target; i++) {
            cand.push_back(candidates[i]);
            dfs(candidates, target-candidates[i], ans, cand, i);
            cand.pop_back();
        }
    }
};
