/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const n = matrix.length;
    if (n == 0) return [];
    let r = Array(matrix[0].length).fill().map(() => Array());
    for (let i=1;i<n;++i) {
        const m = matrix[i].length;
        for (let j=0;j<m;++j) {
            r[m-j-1].push(matrix[i][j]);
        }
    }
    return matrix[0].concat(spiralOrder(r));
};
