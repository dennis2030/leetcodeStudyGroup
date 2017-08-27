class Solution {
public:
	int countNumbersWithUniqueDigits(int n) {
		if (n == 0) return 1;
		int ans = 1, p = 9, unique = 9;
		int m = min(n, 10);
		for (int i = 0; i < n; i++) {
			ans += unique;
			unique *= p;
			p--;
		}

		return ans;
	}
};
