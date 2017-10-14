class Solution {
public:
	int evalRPN(vector<string>& tokens) {
		stack<int> tmp;
		for (auto token: tokens) {
			int n1, n2;
			bool isPop = false;
			if (tmp.size() >= 2) {
				n2 = tmp.top();
				tmp.pop();
				n1 = tmp.top();
				tmp.pop();
				isPop = true;
			}
			if (token == "+") {
				tmp.push(n1 + n2);
			} else if (token == "-") {
				tmp.push(n1 - n2);
			} else if (token == "*") {
				tmp.push(n1 * n2);
			} else if (token == "/") {
				tmp.push(n1 / n2);
			} else {
				if (isPop) {
					tmp.push(n1);
					tmp.push(n2);
				}
				tmp.push(stoi(token));
			}
		}

		return tmp.top();
	}
};
