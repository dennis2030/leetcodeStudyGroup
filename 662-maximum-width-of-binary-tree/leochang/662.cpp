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
    int widthOfBinaryTree(TreeNode* root) {
        int ans = 0;
        unordered_map<int, int> leftest;
        dfs(root, ans, 1, 1, leftest);
        return ans;
    }
    void dfs(TreeNode *node, int &ans, int id, int level, unordered_map<int, int> &leftest) {
        if (node == NULL) {
            return;
        }
        if (leftest.size() < level) {
            leftest[level] = id;
        }

        ans = max(ans, id - leftest[level]+1);
        dfs(node->left, ans, id*2, level+1, leftest);
        dfs(node->right, ans, id*2+1, level+1, leftest);
    }
};
