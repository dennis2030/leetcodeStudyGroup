/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var constructArray = function(n, k) {
    let ans = [];
    let start = 1, end = k + 1;
    for (let i = 1; i <= k + 1; i++) {
        if (i % 2 !== 0) {
            ans.push(start);
            start += 1;
        } else {
            ans.push(end);
            end -= 1;
        }
    }
    for (let i = k + 2; i <= n; i++) {
        ans.push(i);
    }
    return ans;
};
