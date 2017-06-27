/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    function f(n) {
        if (n === null) return false;
        let a = f(n.left), b = f(n.right);
        if (n === p || n === q) return ((a || b) && n) || true;
        else if (a && b) return n;
        else return (a || b);
    }
    return f(root);
};
