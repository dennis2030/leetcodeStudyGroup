/**
 * @param {number[]} A
 * @return {number}
 */
var maxRotateFunction = function(A) {
    let max = 0, sum = 0, len = A.length;
    for (let i = 0; i < len; i++) {
        max += (i * A[i]);
        sum += A[i];
    }
    let local = max;
    for (let i = len - 1; i > 0; i--) {
        local = local + sum - len * A[i];
        max = Math.max(max, local);
    }
    return max;
};