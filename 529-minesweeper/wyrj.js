/**
 * @param {character[][]} board
 * @param {number[]} click
 * @return {character[][]}
 */
var updateBoard = function(board, click) {
    let rowCount = board.length;
    let colCount = board[0].length;
    function flood(r, c, callback) {
        let startRow = r > 0 ? (r - 1) : 0;
        let startCol = c > 0 ? (c - 1) : 0;
        let endRow = r < rowCount - 1 ? (r + 1) : (rowCount - 1);
        let endCol = c < colCount - 1 ? (c + 1) : (colCount - 1);
        for (let i = startRow; i <= endRow; i++) {
            for (let j = startCol; j <= endCol; j++) {
                if (i !== r || j !== c) callback(i, j);
            }
        }
    }
    function calcNumber(r, c) {
        let count = 0;
        flood(r, c, (row, col) => {
            if (board[row][col] === 'M') count += 1;
        });
        return count;
    }
    function clickBoard(r, c) {
        if (board[r][c] !== 'M' && board[r][c] !== 'E') return;
        if (board[r][c] === 'M') {
            board[r][c] = 'X';
            return;
        }
        let n = calcNumber(r, c);
        if (n > 0) {
            board[r][c] = n.toString();
            return;
        }
        board[r][c] = 'B';
        flood(r, c, clickBoard);
        
    }
    clickBoard(click[0], click[1]);
    return board;
};
