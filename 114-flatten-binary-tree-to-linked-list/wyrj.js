/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    function f(node) {
        let l, r;
        if (node.left) l = f(node.left);
        if (node.right) r = f(node.right);
        if (l) {
            l.right = node.right;
            node.right = node.left;
            node.left = null;
        }
        return r || l || node;
    }
    if (root) f(root);
};
