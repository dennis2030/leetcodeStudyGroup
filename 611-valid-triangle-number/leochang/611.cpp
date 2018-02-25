class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        if (nums.size() < 3) return 0;
        vector<int> snums(nums);
        int ans = 0;
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i < nums.size()-2; i++) {
            for(int j = i+1, k = i+2; k < nums.size(); k++) {
                while(j < k && nums[i]+nums[j] <= nums[k]) j++;
                ans += k -j;
            }
        }
        
        return ans;
    }
};
