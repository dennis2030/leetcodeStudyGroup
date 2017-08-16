class Solution {
    vector<int> _nums;
public:
    Solution(vector<int> nums) {
        _nums = nums;
    }
    
    int pick(int target) {
        int x, c = 1;
        for (int i=0; i<_nums.size(); ++i) {
            if (_nums[i] != target) continue;
            if (rand()%c == 0) x = i;
            c++;
        }
        return x;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
