class Solution {
public:
	int lastRemaining(int n) {
		return FromLeftToRight(n);
	}
private:
	int FromLeftToRight(int n) {
		if (1 == n) {
			return n;
		}

		return 2 * FromRightToLeft(n/2);
	}

	int FromRightToLeft(int n) {
		if (1 == n) {
			return 1;
		}

		if (0 == n % 2) {
			return 2 * FromLeftToRight(n/2) - 1;
		} else {
			return 2 * FromLeftToRight(n/2);
		}
	}
};
