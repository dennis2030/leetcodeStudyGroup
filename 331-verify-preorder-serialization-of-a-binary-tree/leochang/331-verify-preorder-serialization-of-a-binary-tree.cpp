class Solution {
public:
	bool isValidSerialization(string preorder) {
		if (preorder.empty() || (preorder[0] == '#' && preorder.size() > 1)) {
			return false;
		}

		int size = preorder.size();
		int count = 1;

		for (int i = 0; i < size; i++) {
			if (preorder[i] == ',') {
				continue;
			}

			if (preorder[i] == '#') {
				count--;
			} else if (i == 0 || preorder[i-1] == ','){
				count++;
			}

			if (count < 0 || (count == 0 && i != size-1)) {
				return false;
			}
		}

		return (count == 0);
	}
};
