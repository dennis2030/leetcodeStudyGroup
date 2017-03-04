class Solution {
public:
    int threeSumClosestZero(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int best = nums[0] + nums[1] + nums[2];
        for (auto it = nums.begin(); it != nums.end() - 2; ++it) {
            for (auto jt = it + 1, kt = nums.end() - 1; jt != kt; ) {
                int battle = *it + *jt + *kt;
                if (abs(battle) < abs(best)) {
                    best = battle;
                }
                if (battle == 0) {
                    return 0;
                } if (battle < 0) {
                    ++jt;
                } else if (battle > 0) {
                    --kt;
                }
            }
        }
        return best;
    }

    int threeSumClosest(vector<int> &nums, int target) {
        vector<int> normalized;
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            int shifted = (*it * 3) - target;
            normalized.push_back(shifted);
        }
        return (threeSumClosestZero(normalized) + target * 3) / 3;
    }
};
