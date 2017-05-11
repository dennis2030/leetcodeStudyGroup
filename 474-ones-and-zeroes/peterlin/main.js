/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function(strs, m, n) {
    var a = strs.map((s) => {
        return [s.split("0").length-1, s.split("1").length-1];
    });
    var p = Array(m+1).fill(0).map((x) => { return Array(n+1).fill(0); });
    a.forEach((x) => {
        for(var i=m;i>=x[0];--i) {
            for(var j=n;j>=x[1];--j) {
                p[i][j] = Math.max(p[i-x[0]][j-x[1]]+1, p[i][j]);
            }
        }
    });
    return p[m][n];
};
