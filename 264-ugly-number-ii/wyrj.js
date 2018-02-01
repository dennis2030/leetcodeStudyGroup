/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    let arr = [1];
    let indices = new Array(6).fill(0);
    while (arr.length < n) {
        let next = Number.MAX_SAFE_INTEGER;
        next = Math.min(2 * arr[indices[2]], 3 * arr[indices[3]], 5 * arr[indices[5]]);
        if (next === 2 * arr[indices[2]]) indices[2] += 1;
        if (next === 3 * arr[indices[3]]) indices[3] += 1;
        if (next === 5 * arr[indices[5]]) indices[5] += 1;
        arr.push(next);
    }
    return arr[n - 1];
};
