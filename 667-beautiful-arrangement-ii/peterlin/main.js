/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var constructArray = function(n, k) {
    var s = [1];
    for (var i=k, r=1; i>0; --i, r=-r) {
        s.push(s[s.length-1] + r*i);
    }
    for (var i=k+2; i<=n; ++i) {
        s.push(i);
    }
    return s;
};
