/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    var v = Array(9).fill().map(x => Array(10).fill(false));
    var h = Array(9).fill().map(x => Array(10).fill(false));
    var r = Array(9).fill().map(x => Array(10).fill(false));
    for (var i=0;i<9;++i) {
        for (var j=0;j<9;++j) {
            var n = parseInt(board[i][j]);
            if (isNaN(n)) continue;
            if (v[i][n]) return false;
            if (h[j][n]) return false;
            if (r[Math.floor(i/3)*3+Math.floor(j/3)][n]) return false;
            v[i][n] = h[j][n] = r[Math.floor(i/3)*3+Math.floor(j/3)][n] = true;
        }
    }
    return true;
};
