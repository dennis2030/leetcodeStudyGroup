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
    if (root === null) return [];
    let queue = [root];
    let ans = [[]];
    let depth = 0, index = 1;
    for (let i = 0; i < queue.length; i++) {
        if (i >= index) {
            depth += 1;
            ans[depth] = [];
            index = queue.length;
        }
        ans[depth].push(queue[i].val);
        if (queue[i].left) queue.push(queue[i].left);
        if (queue[i].right) queue.push(queue[i].right);
    }
    return ans;
};