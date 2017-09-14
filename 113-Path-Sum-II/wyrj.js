/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
    let ans = [];
    let q = [];
    function dfs(node, total) {
        total += node.val;
        q.push(node.val);
        if (total === sum && node.left === null && node.right === null) ans.push(q.slice());
        if (node.left) dfs(node.left, total);
        if (node.right) dfs(node.right, total);
        q.pop();
    }
    if (root) dfs(root, 0);
    return ans;
};
