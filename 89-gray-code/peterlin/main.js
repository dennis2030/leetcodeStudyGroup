/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    if (n === 0) return [0];
    var s = grayCode(n-1);
    var p = [];
    for (var i=0;i<s.length;++i) { p.push(s[i]); }
    for (var i=0;i<s.length;++i) { p.push(s[s.length-i-1]+Math.pow(2, n-1)); }
    return p;
};
