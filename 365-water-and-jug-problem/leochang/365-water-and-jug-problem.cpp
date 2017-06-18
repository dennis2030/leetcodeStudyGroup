class Solution {
public:
	bool canMeasureWater(int x, int y, int z) {
		if (x + y < z) {
			return false;
		}
		if (0 == z || x + y == z) {
			return true;
		}

		return 0 == (z % gcd(x, y));
	}
private:
	int gcd(int x, int y) {
		while (0 != y) {
			int tmp = y;
			y = x % y;
			x = tmp;
		}
		return x;
	}
};
