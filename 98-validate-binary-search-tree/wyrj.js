/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    function f(n, l, r) {
        return !n || ((!l || l.val < n.val) && f(n.left, l, n) && (!r || n.val < r.val) && f(n.right, n, r));
    }
    return f(root);
};
