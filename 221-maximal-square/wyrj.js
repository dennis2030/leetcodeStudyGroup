/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    var max = 0, table = [];
    var r, c;
    table[-1] = [];
    for (r = 0; r < matrix.length; r++) {
        table[r] = [];
        for (c = 0; c < matrix[0].length; c++) {
            if (matrix[r][c] === '0') {
                table[r][c] = 0;
            } else {
                table[r][c] = Math.min(table[r][c - 1] || 0, table[r - 1][c] || 0, table[r - 1][c - 1] || 0) + 1;
                if (table[r][c] > max) {
                    max = table[r][c];
                }
            }
        }
    }
    return max * max;
};