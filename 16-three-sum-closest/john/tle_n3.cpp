class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int best = nums[0] + nums[1] + nums[2];
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            for (auto jt = it + 1; jt != nums.end(); ++jt) {
                for (auto kt = jt + 1; kt != nums.end(); ++kt) {
                    int battle = *it + *jt + *kt;
                    if (abs(target - battle) < abs(target - best)) {
                        best = battle;
                    }
                }
            }
        }
        return best;
    }
};
