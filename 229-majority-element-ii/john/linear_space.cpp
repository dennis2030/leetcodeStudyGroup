class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        map<int, int> counts;
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            ++counts[*it];
        }
        vector<int> results;
        for (auto it = counts.begin(); it != counts.end(); ++it) {
            if (it->second > nums.size() / 3) {
                results.push_back(it->first);
            }
        }
        return results;
    }
};
