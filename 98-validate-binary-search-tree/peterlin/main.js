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
    var f = (node, l, h) => {
        if (node === null) return true;
        if (l !== null && node.val <= l) return false;
        if (h !== null && node.val >= h) return false;
        return f(node.left, l, node.val) && f(node.right, node.val, h);
    };
    return f(root, null, null);
};
