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
	TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
		if (preorder.empty() || inorder.empty()) return nullptr;
		return helper(preorder, inorder, 0, preorder.size()-1, 0, inorder.size()-1);
	}
	TreeNode* helper(vector<int>& preorder, vector<int>& inorder, int pLeft, int pRight, int iLeft, int iRight) {
		if (pLeft > pRight) return nullptr;
		TreeNode* root = new TreeNode(preorder[pLeft]);
		int idx = findIdx(preorder, inorder, preorder[pLeft]);
		root->left = helper(preorder, inorder, pLeft+1, pLeft+idx-iLeft, iLeft, idx-1);
		root->right = helper(preorder, inorder, pLeft+idx-iLeft+1, pRight, idx+1, iRight);
		return root;
	}
	int findIdx(vector<int>& preorder, vector<int>& inorder, int val) {
		int idx = 0;
		for (;idx < inorder.size(); idx++) {
			if (inorder[idx] == val) break;
		}
		return idx;
	}
};
