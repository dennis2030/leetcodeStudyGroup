class Solution {
public:
    int nthUglyNumber(int n) {
        int count = 0;
        long ans = 0;
        priority_queue<long, vector<long>, greater<long>> uglyNum;
        uglyNum.push(1);
            
        while (count < n) {
            ans = uglyNum.top();
            uglyNum.pop();
            while (!uglyNum.empty() && ans == uglyNum.top()) uglyNum.pop();
            uglyNum.push(ans*2);
            uglyNum.push(ans*3);
            uglyNum.push(ans*5);
            count++;
        }
        
        return ans;
    }
};
