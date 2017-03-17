/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
function Node(left, right) {
    this.left = left || null;
    this.right = right || null;
}
/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var generateTrees = function(n) {
    if (n === 0) return [];
    var trees = [], layer, i, leftIndex, leftLayer, rightIndex, rightLayer;
    trees[0] = [null];
    for (layer = 1; layer <= n; layer++) {
        trees[layer] = [];
        for (i = 0; i < layer; i++) {
            leftLayer = trees[i];
            rightLayer = trees[layer - i - 1];
            for (leftIndex = 0; leftIndex < leftLayer.length; leftIndex++) {
                for (rightIndex = 0; rightIndex < rightLayer.length; rightIndex++) {
                    trees[layer].push(new Node(leftLayer[leftIndex], rightLayer[rightIndex]));
                }
            }
        }
    }
    var fillNumber = function(node, treeNode, number) {
        if (node.left) {
            treeNode.left = new TreeNode(0);
            number = fillNumber(node.left, treeNode.left, number);
        }
        treeNode.val = number;
        number += 1;
        if (node.right) {
            treeNode.right = new TreeNode(0);
            number = fillNumber(node.right, treeNode.right, number);
        }
        return number;
    };
    var treeNodes = [];
    trees[n].forEach(function(node) {
        var treeNode = new TreeNode(0);
        fillNumber(node, treeNode, 1);
        treeNodes.push(treeNode);
    });
    return treeNodes;
};