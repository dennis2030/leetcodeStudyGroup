class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        recursive(nums, ans, 0);
        return ans;
    }
    void recursive(vector<int> &nums, vector<vector<int>> &ans, int idx) {
        if (idx == nums.size()) {
            ans.push_back(nums);
        }
        for (int i = idx; i < nums.size(); i++) {
            swap(nums[idx], nums[i]);
            recursive(nums, ans, idx+1);
            swap(nums[idx], nums[i]);
        }
    }
};
