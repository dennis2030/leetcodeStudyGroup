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
    var val = preorder.shift();
    var index = inorder.indexOf(val);
    var node = new TreeNode(val);
    node.left = buildTree(preorder, inorder.slice(0, index));
    node.right = buildTree(preorder, inorder.slice(index+1));
    return node;
};
