class Solution {
public:
	string getHint(string secret, string guess) {
		if (secret.empty()) return "0A0B";
		int A = 0, B = 0;
		vector<bool> isA(guess.size(), false);
		vector<bool> isMatch(secret.size(), false);

		for(int i = 0; i < guess.size(); i++) {
			if (guess[i] == secret[i]) {
				A++;
				isMatch[i] = true;
				isA[i] = true;
				continue;
			}
		}
		for(int i = 0; i < guess.size(); i++) {
			if (isA[i]) continue;
			for (int j = 0; j < secret.size(); j++) {
				if (guess[i] == secret[j] && !isMatch[j]) {
					isMatch[j] = true;
					B++;
					break;
				}
			}
		}

		stringstream ss;
		ss << A << "A" << B << "B";
		return ss.str();
	}
};
