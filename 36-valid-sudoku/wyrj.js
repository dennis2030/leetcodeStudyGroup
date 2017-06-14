var setFlag = function(flag, i) {
    if ('.' !== i && flag[i]) {
        return false;
    }
    flag[i] = true;
    return true;
}
var checkRow = function(board, row) {
    var flag = []
    var i, n;
    for (i = 0; i < 9; i++) {
        n = board[row][i];
        if (!setFlag(flag, n)) {
            return false;
        }
    }
    return true;
}
var checkCol = function(board, col) {
    var flag = []
    var i, n;
    for (i = 0; i < 9; i++) {
        n = board[i][col];
        if (!setFlag(flag, n)) {
            return false;
        }
    }
    return true;
}
var checkGroup = function(board, row, col) {
    var flag = [];
    var i, j, n;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            n = board[row + i][col + j];
            if (!setFlag(flag, n)) {
               return false;
            }
        }
    }
    return true;
}
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    var i, j;
    for (i = 0; i < 9; i++) {
        if (!checkRow(board, i) || !checkCol(board, i)) {
            return false;
        }
    }
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if (!checkGroup(board, i * 3, j * 3)) {
                return false;
            }
        }
    }
    return true;
};