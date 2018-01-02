/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let ans = [];
    let f = (c, m, n) => {
        if (m <= 0 || n <= 0) return;
        for (let i = 0; i < m; i++) {
            c.col += 1;
            ans.push(matrix[c.row][c.col]);
        }

        if (n === 1) return;
        for (let i = 0; i < n - 1; i++) {
            c.row += 1;
            ans.push(matrix[c.row][c.col]);
        }
        
        if (m === 1) return;
        for (let i = 0; i < m - 1; i++) {
            c.col -= 1;
            ans.push(matrix[c.row][c.col]);
        }
        
        if (n === 2) return;
        for (let i = 0; i < n - 2; i++) {
            c.row -= 1;
            ans.push(matrix[c.row][c.col]);
        }
        f(c, m - 2, n - 2);
    }
    if (matrix.length && matrix[0].length) {
        f({row: 0, col: -1}, matrix[0].length, matrix.length);
    }
    return ans;
};
