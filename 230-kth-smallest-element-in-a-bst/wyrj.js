/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    let count = k, ans;
    function dfs(node) {
        if (node.left) dfs(node.left);
        count -= 1;
        if (count === 0) ans = node.val;
        else if (node.right) dfs(node.right);
    }
    dfs(root);
    return ans;
};
