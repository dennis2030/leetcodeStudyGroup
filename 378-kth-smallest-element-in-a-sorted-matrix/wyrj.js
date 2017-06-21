/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(matrix, k) {
    const n = matrix.length;
    let min = matrix[0][0];
    let max = matrix[n - 1][n - 1];
    while (min < max) {
        let mid = Math.floor((min + max) / 2);
        let j = n - 1;
        let count = 0;
        for (let i = 0; i < n; i++) {
            while (j >= 0 && matrix[i][j] > mid) {
                j--;
            }
            count += (j + 1);
        }
        if (count < k) min = mid + 1;
        else max = mid;
    }
    return min;
};
