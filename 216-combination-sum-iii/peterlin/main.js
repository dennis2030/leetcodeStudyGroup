/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    const ans = [];
    const f = (i, arr) => {
        if (arr.length === k) {
            if (n === arr.reduce((a, b) => a + b, 0)) ans.push(arr);
            return;
        }
        for (;i<=9;++i) f(i+1, arr.concat(i));
    };
    f(1, []);
    return ans;
};
