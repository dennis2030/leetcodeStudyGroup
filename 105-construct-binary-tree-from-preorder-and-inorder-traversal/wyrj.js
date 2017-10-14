/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    if (inorder.length === 0) return null;
    let v = preorder.shift();
    let node = new TreeNode(v);
    let idx = inorder.indexOf(v);
    node.left = buildTree(preorder, inorder.slice(0, idx));
    node.right = buildTree(preorder, inorder.slice(idx + 1, inorder.length));
    return node;
};
