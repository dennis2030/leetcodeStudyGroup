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
    var stack = [];
    var f = (node) => {
        if (node === null) return null;
        var left = f(node.left);
        var right = f(node.right);
        node.left = null;
        if (left !== null) {
            node.right = left;
            while (left.right !== null) left = left.right;
            left.right = right;
        } else {
            node.right = right;
        }
        return node;
    };
    f(root);
};
