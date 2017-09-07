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
    var c = 0, x = null;
    var f = (node) => {
        if (x !== null) return;
        if (node.left != null) f(node.left);
        if (++c === k) {
            x = node.val;
        }
        if (node.right != null) f(node.right);
    };
    f(root);
    return x;
};
