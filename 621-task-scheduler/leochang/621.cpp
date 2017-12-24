class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> taskMaps;
        for (auto c : tasks) {
            taskMaps[c]++;
        }
        
        int maxTasks = 0;
        int maxTaskCount = 0;
        
        for (auto& kv : taskMaps) {
            maxTasks = max(maxTasks, kv.second);
        }
        
        for (auto& kv : taskMaps) {
            if (kv.second == maxTasks) maxTaskCount++;
        }
        
        return max((int)tasks.size(), (maxTasks-1)*(n+1) + maxTaskCount);
    }
};
