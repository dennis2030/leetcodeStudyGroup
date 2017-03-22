/**
 * @param {number[]} A
 * @return {number}
 */
var maxRotateFunction = function(A) {
    var sum = A.reduce((t, c) => { return t+c; }, 0);
    var ans = A.reduce((t, c, i) => { return t+c*i; }, 0);
    var v = ans;
    for (var i=A.length-1;i>0;--i) {
        v += sum - A[i]*A.length;
        ans = Math.max(ans, v);
    }
    return ans;
};
