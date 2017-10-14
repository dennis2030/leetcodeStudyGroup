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
	int kthSmallest(TreeNode* root, int k) {
		return InOrderTraverse(root, k);
	}
private:
	int InOrderTraverse(TreeNode* root, int &k) {
		if (root == NULL) return -1;
		int ans = InOrderTraverse(root->left, k);
		k--;
		if (k == 0) return root->val;
		if (ans == -1) ans = InOrderTraverse(root->right, k);
		return ans;
	}
};
