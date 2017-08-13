class Solution {
public:
	string fractionAddition(string expression) {
		int ans_n = 0, ans_d = 1;
		int tmp_n = 0, tmp_d = 0;
		char slash;
		istringstream in(expression);

		while (in >> tmp_n >> slash >> tmp_d) {
			auto gcd = abs(GCD(ans_d, tmp_d));
			ans_n = (ans_n * tmp_d + tmp_n * ans_d) / gcd;
			ans_d = ans_d * tmp_d / gcd;
		}
		auto gcd = abs(GCD(ans_n, ans_d));
		return to_string(ans_n/gcd) + '/' + to_string(ans_d/gcd);
	}
	int GCD(int a, int b){
		return (b == 0) ? a : GCD(b, a % b);
	}
};
