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
    var minT = [];
    var maxT = [];
    var f = (dep, pos, node) => {
        if (node === null) return;
        if (dep === minT.length) minT.push(pos);
        else if (minT[dep] > pos) minT[dep] = pos;
        if (dep === maxT.length) maxT.push(pos);
        else if (maxT[dep] < pos) maxT[dep] = pos;
        f(dep+1, pos*2, node.left);
        f(dep+1, pos*2+1, node.right);
    };
    
    while (root != null) {
        if (root.left !== null && root.right !== null) break;
        if (root.left !== null) root = root.left;
        else if (root.right !== null) root = root.right;
        else break;
    }
    
    f(0, 0, root);
    
    var x = 1;
    for (var i=0;i<minT.length;++i) {
        x = Math.max(x, maxT[i]-minT[i]+1);
    }
    return x;
};
