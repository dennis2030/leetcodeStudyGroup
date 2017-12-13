/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const ans = [[]];
    function p(n, arr) {
        if (!ans[n]) {
            ans[n] = [];
        }
        ans[n].push(arr);
    };
    for (let i = 0; i < candidates.length; i++) {
        const n = candidates[i];
        p(n, [n]);
        for (let j = 1; j <= target - n; j++) {
            if (!ans[j]) {
                continue;
            }
            for (let k = 0; k < ans[j].length; k++) {
                let copy = ans[j][k].slice();
                copy.push(n);
                p(j + n, copy);
            }
        }
    }
    return ans[target] || [];
};
