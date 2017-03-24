/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */
TreeNode.prototype.assign = function(left, right) {
    this.left = left;
    this.right = right ? right.addon(this.val) : null;
    return this;
};
TreeNode.prototype.addon = function(n) {
    let node = new TreeNode(this.val + n);
    if (this.left) node.left = this.left.addon(n);
    if (this.right) node.right = this.right.addon(n);
    return node;
}
var generateTrees = function(n) {
    var trees = [], layer, i, leftIndex, leftLayer, rightIndex, rightLayer;
    trees[0] = [null];
    for (layer = 1; layer <= n; layer++) {
        trees[layer] = [];
        for (i = 0; i < layer; i++) {
            leftLayer = trees[i];
            rightLayer = trees[layer - i - 1];
            for (leftIndex = 0; leftIndex < leftLayer.length; leftIndex++) {
                for (rightIndex = 0; rightIndex < rightLayer.length; rightIndex++) {
                    trees[layer].push(new TreeNode(i + 1).assign(leftLayer[leftIndex], rightLayer[rightIndex]));
                }
            }
        }
    }
    return n === 0 ? [] : trees[n];
};