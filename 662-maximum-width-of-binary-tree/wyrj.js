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
var widthOfBinaryTree = function(root) {
    if (!root) return 0;
    const q = [{n: root, v: 1}];
    let cut = 0, max = 0, s = -1;
    for (let i = 0; i < q.length; i++) {
        if (q[i].n.left) {
            if (s === -1) {
                s = (q[i].v - 1) * 2;
            }
            q.push({n: q[i].n.left, v: q[i].v * 2 - 1 - s});
        }
        if (q[i].n.right) {
            if (s === -1) {
                s = (q[i].v - 1) * 2 + 1;
            }
            q.push({n: q[i].n.right, v: q[i].v * 2 - s});
        }
        if (i === cut) {
            max = Math.max(max, q[i].v);
            cut = q.length - 1;
            s = -1;
        }
    }
    return max;
};
