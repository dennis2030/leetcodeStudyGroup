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
	vector<vector<int>> levelOrder(TreeNode* root) {
		vector<vector<int> >  vResult;
		vector<int> vRow;
		queue<TreeNode*> qInProcess;
		qInProcess.push(root);
		int size = 1;

		if(NULL == root) return vResult;

		while(!qInProcess.empty()) {
			if (qInProcess.front()->left) {
				qInProcess.push(qInProcess.front()->left);
			}
			if (qInProcess.front()->right) {
				qInProcess.push(qInProcess.front()->right);
			}

			vRow.emplace_back(qInProcess.front()->val);
			qInProcess.pop();
			size--;

			if (0 == size) {
				vResult.push_back(vRow);
				vRow.clear();
				size = qInProcess.size();
			}
		}

		return vResult;
	}
};
