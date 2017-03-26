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
	vector<TreeNode*> recursive(int begin, int end) {
		vector<TreeNode *> ret;
		for (int i = begin; i <= end; ++i){
			auto leftTree = (i == begin) ? vector<TreeNode*>{nullptr} : recursive (begin, i-1);
			auto rightTree = (i == end) ? vector<TreeNode*>{nullptr} : recursive (i+1, end);
			for(auto left : leftTree){
				for (auto right: rightTree){
					TreeNode *node = new TreeNode (i);
					node->left = left;
					node->right = right;
					ret.push_back(node);
				}
			}
		}
		return ret;
	}
	vector<TreeNode*> generateTrees(int n) {
		if (n == 0) {
			vector<TreeNode*> ret;
			return ret;
		}
		return recursive(1, n);
	}
};
