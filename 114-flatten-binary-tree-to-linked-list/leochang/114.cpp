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
	void flatten(TreeNode* root) {
		if (root == NULL) return;

		TreeNode* leftNode = root->left;
		TreeNode* rightNode = root->right;

		flatten(leftNode);
		flatten(rightNode);

		root->left = NULL;
		root->right = leftNode;

		TreeNode* tmp = root;

		while (tmp->right != NULL){
			tmp = tmp->right;
		}

		tmp->right = rightNode;
	}
};
