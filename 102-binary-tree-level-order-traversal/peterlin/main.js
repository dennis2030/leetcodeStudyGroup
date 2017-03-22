/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    var p = [], q = [[root, 0]];
    while (q.length > 0) {
        var c = q.shift();
        if (c[0] === null) continue;
        if (!(c[1] in p)) p[c[1]] = [];
        p[c[1]].push(c[0].val);
        q.push([c[0].left, c[1]+1]);
        q.push([c[0].right, c[1]+1]);
    }
    return p;
};
