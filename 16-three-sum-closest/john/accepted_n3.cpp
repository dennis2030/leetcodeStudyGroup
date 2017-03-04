class Solution {
public:
    int threeSumClosestZero(vector<int> &all,
            vector<int> &zeros, vector<int> &nonzeros,
            vector<int> &positives, vector<int> &negatives) {
        if (zeros.size() >= 3) {
            return 0;
        }

        sort(positives.begin(), positives.end());
        sort(negatives.begin(), negatives.end(), greater<int>());

        if (positives.empty()) {
            return accumulate(negatives.begin(), negatives.begin() + (3 - zeros.size()), 0);
        }
        if (negatives.empty()) {
            return accumulate(positives.begin(), positives.begin() + (3 - zeros.size()), 0);
        }

        int best = all[0] + all[1] + all[2];

        if (zeros.size() == 2) {
            for (auto it = nonzeros.begin(); it != nonzeros.end(); ++it) {
                int battle = *it;
                if (abs(battle) < abs(best)) {
                    best = battle;
                }
            }
        }

        if (zeros.size() >= 1) {
            for (auto it = positives.begin(); it != positives.end(); ++it) {
                for (auto jt = negatives.begin(); jt != negatives.end(); ++jt) {
                    int battle = *it + *jt;
                    if (abs(battle) < abs(best)) {
                        best = battle;
                    }
                }
            }
        }

        for (auto it = positives.begin(); it != positives.end(); ++it) {
            for (auto jt = it + 1; jt != positives.end(); ++jt) {
                for (auto kt = negatives.begin(); kt != negatives.end(); ++kt) {
                    int battle = *it + *jt + *kt;
                    if (abs(battle) < abs(best)) {
                        best = battle;
                    }
                }
            }
        }
        for (auto it = negatives.begin(); it != negatives.end(); ++it) {
            for (auto jt = it + 1; jt != negatives.end(); ++jt) {
                for (auto kt = positives.begin(); kt != positives.end(); ++kt) {
                    int battle = *it + *jt + *kt;
                    if (abs(battle) < abs(best)) {
                        best = battle;
                    }
                }
            }
        }

        return best;
    }
    int threeSumClosest(vector<int> &nums, int target) {
        vector<int> all, zeros, nonzeros, positives, negatives;
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            int shifted = (*it * 3) - target;
            all.push_back(shifted);
            if (shifted == 0) {
                zeros.push_back(shifted);
            } else {
                nonzeros.push_back(shifted);
            }
            if (shifted > 0) {
                positives.push_back(shifted);
            }
            if (shifted < 0) {
                negatives.push_back(shifted);
            }
        }
        return (threeSumClosestZero(all, zeros, nonzeros, positives, negatives) + target * 3) / 3;
    }
};
