class Solution {
public:
    bool isUgly(int num) {
        if (0 >= num) return false;
        int primes[3] = {2, 3, 5};
        for (auto prime: primes) {
            while (0 == num % prime) {
                num = num / prime;
            }
        }
        return (1 == num);
    }
};
