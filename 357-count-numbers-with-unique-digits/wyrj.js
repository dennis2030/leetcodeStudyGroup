/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    let ans = 1, base = 9, next = 9, m = Math.min(n, 10);
    for (let i = 0; i < m; i++) {
        ans += base;
        base *= next;
        next -= 1;
    }
    return ans;
};
