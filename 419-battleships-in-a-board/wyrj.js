/**
 * @param {character[][]} board
 * @return {number}
 */
var countBattleships = function(board) {
    let count = 0;
    let rLen = board.length;
    let cLen = board[0].length;
    for (let r = 0; r < rLen; r++) {
        for (let c = 0; c < cLen; c++) {
            if (board[r][c] === 'X' && (r === rLen - 1 || board[r + 1][c] !== 'X') && (c === cLen - 1 || board[r][c+ 1] !== 'X')) {
                count++;
            }
        }
    }
    return count;
};