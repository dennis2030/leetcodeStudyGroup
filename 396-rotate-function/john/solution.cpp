class Solution {
public:
    int F0(vector<int> &A) {
        int sum = 0;
        for (int i = 0; i < A.size(); ++i) {
            sum += i * A.at(i);
        }
        return sum;
    }

    int calcNextF(int n, int curr, int total, int tail) {
        return curr + total - tail * n;
    }

    int maxRotateFunction(vector<int> &A) {
        int total = accumulate(A.begin(), A.end(), 0);
        int n = A.size();
        int curr = F0(A);
        int best = curr;

        for (int i = 1; i < A.size(); ++i) {
            int battle = calcNextF(n, curr, total, A.at(n - i));
            curr = battle;
            best = max(battle, best);
        }

        return best;
    }
};
