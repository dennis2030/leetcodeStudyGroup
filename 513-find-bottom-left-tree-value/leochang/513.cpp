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
	int findBottomLeftValue(TreeNode* root) {
		int maxDepth = 0;
		int ans = root->val;
		findBottomLeftValue(root, 0, maxDepth, ans);
		return ans;
	}
private:
	void findBottomLeftValue(TreeNode* root, int depth, int &maxDepth, int &ans) {
		if (root == NULL) return;

		findBottomLeftValue(root->left, depth + 1, maxDepth, ans);
		findBottomLeftValue(root->right, depth + 1, maxDepth, ans);

		if (depth > maxDepth) {
			maxDepth = depth;
			ans = root->val;
		}
	}
};
