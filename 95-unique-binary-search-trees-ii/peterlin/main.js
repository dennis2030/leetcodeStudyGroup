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
var generateTrees = function(n) {
    var f = (n, st) => {
        if (n === 0) return [null];
        var ans = [];
        for (var i=0;i<n;++i) {
            var lt = f(i, st);
            var rt = f(n-i-1, st+i+1);
            for (var l=0;l<lt.length;++l)
                for (var r=0;r<rt.length;++r) {
                    var x = new TreeNode(st+i);
                    x.left = lt[l];
                    x.right = rt[r];
                    ans.push(x);
                }
        }
        return ans;
    };
    return n===0 ? [] : f(n, 1);
};
