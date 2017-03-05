class Solution {
public:
    bool findTwoDifferentNums(vector<int> &nums, int &num1, int &num2) {
        int found = false;

        num1 = nums[0];
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            if (*it != num1) {
                found = true;
                num2 = *it;
            }
        }

        return found;
    }

    vector<int> majorityElement(vector<int> &nums) {
        vector<int> results;

        if (nums.empty()) {
            return results;
        }

        int candidate1 = 0,
            candidate2 = 0;
        if (!findTwoDifferentNums(nums, candidate1, candidate2)) {
            results.push_back(nums[0]);
            return results;
        }

        int vote1 = 0,
            vote2 = 0;
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            if (*it == candidate1) {
                ++vote1;
            } else if (*it == candidate2) {
                ++vote2;
            } else if (vote1 == 0) {
                candidate1 = *it;
                vote1 = 1;
            } else if (vote2 == 0) {
                candidate2 = *it;
                vote2 = 1;
            } else {
                --vote1;
                --vote2;
            }
        }

        int count1 = 0,
            count2 = 0;
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            if (*it == candidate1) {
                ++count1;
            } else if (*it == candidate2) {
                ++count2;
            }
        }

        if (count1 > nums.size() / 3) {
            results.push_back(candidate1);
        }
        if (count2 > nums.size() / 3) {
            results.push_back(candidate2);
        }

        return results;
    }
};
