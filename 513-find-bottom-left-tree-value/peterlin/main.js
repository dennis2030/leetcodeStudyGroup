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
    var s = [0];
    var q = [root];
    var m = 0;
    for (var i=0;i<q.length;++i) {
        if (s[i] > s[m]) {
            m = i;
        }
        var left = q[i].left;
        if (left !== null) {
            q.push(left);
            s.push(s[i]+1);
        }
        var right = q[i].right;
        if (right !== null) {
            q.push(right);
            s.push(s[i]+1);
        }
    }
    return q[m].val;
};
