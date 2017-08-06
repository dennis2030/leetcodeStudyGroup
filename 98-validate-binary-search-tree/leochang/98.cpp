/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	bool isValidBST(TreeNode* root) {
		if (root == NULL) return true;
		int minVal, maxVal;
		return isValidBSTIn(root, minVal, maxVal);
	}
private:
	bool isValidBSTIn(TreeNode* root, int &min_in, int &max_in) {
		int leftminVal = root->val, leftmaxVal = root->val;
		int rightminVal = root->val, rightmaxVal = root->val;
		bool leftValid = true, rightValid = true;

		if (root->left != NULL) {
			leftValid = isValidBSTIn(root->left, leftminVal, leftmaxVal);
			if (leftmaxVal >= root->val) return false;
			leftminVal = min(root->val, leftminVal);
			leftmaxVal = max(root->val, leftmaxVal);
		}

		if (root->right != NULL) {
			rightValid = isValidBSTIn(root->right, rightminVal, rightmaxVal);
			if (rightminVal <= root->val) return false;
			rightminVal = min(root->val, rightminVal);
			rightmaxVal = max(root->val, rightmaxVal);
		}

		min_in = min(leftminVal, rightminVal);
		max_in = max(leftmaxVal, rightmaxVal);

		return leftValid && rightValid;
	}
};
