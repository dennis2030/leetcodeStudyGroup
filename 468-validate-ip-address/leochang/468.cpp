class Solution {
public:
	string validIPAddress(string IP) {
		if (isIPv4(IP)) {
			return "IPv4";
		} else if (isIPv6(IP)) {
			return "IPv6";
		} else {
			return "Neither";
		}
	}
private:
	bool isIPv4(string IP) {
		if(IP[IP.size()-1] == '.') return false;
		istringstream iss(IP);
		string token;
		int count = 0, v4Count = 0;
		while (getline(iss, token, '.')) {
			bool valid = true;
			for (int i = 0; i < token.size(); i++) {
				if (!isdigit(token[i])) {
					valid = false;
				}
			}
			if (token.size() > 1 && '0' == token[0]) {
				valid = false;
			}
			if (token.size() == 0 || token.size() > 3) {
				valid = false;
			}
			if (valid && stoi(token) < 256) {
				v4Count++;
			}
			count++;
		}
		if (4 == v4Count && 4 == count) {
			return true;
		} else {
			return false;
		}
	}
	bool isIPv6(string IP) {
		if(IP[IP.size()-1] == ':') return false;
		istringstream iss(IP);
		string token;
		int count = 0, v6Count = 0;
		while (getline(iss, token, ':')) {
			if (4 >= token.size() && 0 != token.size()) {
				bool valid = true;
				for (int i = 0; i < token.size(); i++){
					if (string::npos == validIPv6Chars.find(token[i]))
						valid = false;
				}
				if (valid) {
					v6Count++;
				}
			}
			if (0 == count && '0' == token[0]) {
				break;
			}
			count++;
		}
		if (8 == v6Count && 8 == count) {
			return true;
		} else {
			return false;
		}
	}
	const string validIPv6Chars = "0123456789abcdefABCDEF";
};
