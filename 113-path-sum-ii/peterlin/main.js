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
    var arr = [];
    var f = (q, node, val) => {
        if (node === null) {
            return;
        }
        q = q.slice();
        q.push(node.val);
        val -= node.val;
        
        if (node.left === null && node.right === null) {
            if (val === 0) {
                arr.push(q);
            }
            return;
        }
        
        f(q, node.left, val);
        f(q, node.right, val);
    }
    f([], root, sum);
    return arr;
};
