/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const p = Array(target+1).fill().map(() => Array());
    p[0].push([]);
    candidates.forEach(c => {
        for (let i=c;i<=target;++i) {
            p[i-c].forEach(arr => {
                p[i].push(arr.concat([c]));
            });
        }
    });
    return p[target];
};
