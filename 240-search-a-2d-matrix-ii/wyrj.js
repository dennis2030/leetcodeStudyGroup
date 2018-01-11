/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    if (matrix.length === 0) return false;
    let rIndex = 0;
    let cIndex = matrix[0].length - 1;
    while (rIndex < matrix.length && cIndex >= 0) {
        const value = matrix[rIndex][cIndex];
        if (value === target) {
            return true;
        } else if (value < target) {
            rIndex += 1;
        } else {
            cIndex -= 1;
        }
    }
    return false;
};
