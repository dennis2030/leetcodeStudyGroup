/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[][]}
 */
var printTree = function(root) {
    var d = (n) => (n === null ? 0 : Math.max(d(n.left), d(n.right))+1);
    var dep = d(root);

    var tree = Array(dep).fill(0).map(x => Array(Math.pow(2, dep)-1).fill(""));
    var f = (n, x, y) => {
        if (n === null) return;
        tree[y][x] += n.val;
        f(n.left, x-Math.pow(2, dep-y-2), y+1);
        f(n.right, x+Math.pow(2, dep-y-2), y+1);
    };
    f(root, Math.pow(2, dep-1)-1, 0);
    return tree;
};
