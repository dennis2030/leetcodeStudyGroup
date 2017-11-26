class Solution {
public:
    int hIndex(vector<int>& citations) {
        int length = citations.size();
        sort(citations.begin(), citations.end());
        
        for (int i = 0; i < length; i++) {
            if (length-i <= citations[i]) {
                return length-i;
            }
        }
        return 0;
    }
};
