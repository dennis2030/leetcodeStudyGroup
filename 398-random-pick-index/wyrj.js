class Solution {
    vector<int> nums_;
public:
    Solution(vector<int> nums) : nums_(nums) {
        
    }
    
    int pick(int target) {
        int count = 0;
        vector<int> idx;
        for (int i = 0; i < nums_.size(); i++) {
            if (nums_[i] == target) {
                count += 1;
                idx.emplace_back(i);
            }
        }
        return idx[rand() % count];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
