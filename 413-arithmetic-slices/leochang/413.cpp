class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int ret = 0, len = 0;

        for(int i = 2; i < A.size(); i++) {
            if (A[i] - A[i-1] == A[i-1] - A[i-2]) {
                len++;
            } else {
                ret += (len > 0) ? (len+1)*len*0.5 : 0;
                len = 0;
            }
        }
        
        ret += (len > 0) ? (len+1)*len*0.5 : 0;
        return ret;
    }
};
