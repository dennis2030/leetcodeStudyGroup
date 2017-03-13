/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    var i,j;
    for (i in matrix) {
        matrix[i] = matrix[i].map((c) => { return parseInt(c); });
    }
    var ans = 0;
    for (i=0;i<matrix.length;++i) {
        for (j=0;j<matrix[i].length;++j) {
            if (matrix[i][j] === 0) continue;
            if (i > 0 && j > 0) {
                matrix[i][j] = Math.min(matrix[i-1][j-1], Math.min(matrix[i][j-1], matrix[i-1][j]))+1;
            }
            ans = Math.max(ans, matrix[i][j]);
        }
    }
    return ans*ans;
};
