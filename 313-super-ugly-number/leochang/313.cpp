class Solution {
public:
	int nthSuperUglyNumber(int n, vector<int>& primes) {
		int pSize = primes.size();
		vector<int> ugly(n, INT_MAX);
		vector<int> exp(pSize, 0);
		ugly[0] = 1;

		for (int i = 1; i < n; i++){
			for(int j = 0; j < pSize; j++) {
				ugly[i] = min(ugly[i], ugly[exp[j]] * primes[j]);
			}
			for(int j = 0; j < pSize; j++) {
				if(ugly[i] == ugly[exp[j]] * primes[j]) {
					exp[j]++;
				}
			}
		}
		return ugly[n-1];
	}
};
