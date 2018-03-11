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
    vector<vector<string>> printTree(TreeNode* root) {
        int height = getHeight(root);
        int width = pow(2, height) - 1;
        vector<vector<string>> ret(height, vector<string>(width, ""));
        
        dfs(ret, root, 0, 0, width-1);
        
        return ret;
    }
    
    int getHeight(TreeNode* node) {
        return node == nullptr ? 0 : max(getHeight(node->left), getHeight(node->right))+1;
    }
    
    void dfs(vector<vector<string>>& ret, TreeNode* node, int level, int left, int right) {
        if (node == nullptr) return;
        
        int mid = left + (right-left)/2;
        
        ret[level][mid] = to_string(node->val);
        dfs(ret, node->left, level+1, left, mid-1);
        dfs(ret, node->right, level+1, mid+1, right);
    }
};
