/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    var a = new Array(n+1).fill(0);
    for (var i=0;i<n;++i) {
        for (var j=1;i+j*j<=n;++j) {
            if (a[i+j*j] === 0 || a[i+j*j] > a[i]+1) a[i+j*j] = a[i]+1;
        }
    }
    return a[n];
};
