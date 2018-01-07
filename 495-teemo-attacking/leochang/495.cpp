class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int ans = 0;
        if (timeSeries.size() == 0) return 0;
        int end = timeSeries[0];
        for (auto time : timeSeries) {
            if (time < end) {
                ans -= (end - time);
            }
            end = time + duration;
            ans += duration;
        }
        return ans;
    }
};
