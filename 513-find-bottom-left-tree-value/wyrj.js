/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var findBottomLeftValue = function(root) {
    let ans = {n: null, d: -1};
    function dfs(n, d) {
        if (n.left === null && n.right === null) {
            if (d > ans.d) {
                ans.d = d;
                ans.n = n;
            }
            return;
        }
        if (n.left) dfs(n.left, d + 1);
        if (n.right) dfs(n.right, d + 1);
    }
    if (root) dfs(root, 0);
    return ans.n.val;
};
