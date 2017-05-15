/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    let ans = [0];
    let k = 0;
    for (let i = 0; i < n; i++) {
        k = (k << 1) || 1;
        for (let j = 0; j < k; j++) {
            ans[j + k] = ans[k - j - 1] + k;
        }
    }
    return ans;
};