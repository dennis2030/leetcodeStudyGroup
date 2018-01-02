/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    let a = [], ans = [];
    let f = (q, w, e) => {
        if (q === 0) {
            if (w === 0) {
                ans.push(a.slice());
            }
            return;
        }
        if (w < (e + e + q - 1) * q / 2 || w > (9 + 9 - q + 1) * q / 2) {
            return;
        }
        for (let i = e; i <= 9; i++) {
            a.push(i);
            f(q - 1, w - i, i + 1);
            a.pop();
        }
    }
    f(k, n, 1);
    return ans;
};
