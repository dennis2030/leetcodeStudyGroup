/**
 * @param {character[][]} board
 * @param {number[]} click
 * @return {character[][]}
 */
var updateBoard = function(board, click) {
    var x = click[0], y = click[1];
    if (board[x][y] === 'M') {
        board[x][y] = 'X';
    } else {
        var c = 0;
        for (var i=-1;i<2;++i)
            for (var j=-1;j<2;++j) {
                if (x+i < 0 || y+j < 0 || x+i >= board.length || y+j >= board[0].length) continue;
                if (board[x+i][y+j] === 'M') ++c;
            }
        if (c > 0) {
            board[x][y] = ''+c;
        } else {
            board[x][y] = 'B';
            for (var i=-1;i<2;++i)
                for (var j=-1;j<2;++j) {
                    if (x+i < 0 || y+j < 0 || x+i >= board.length || y+j >= board[0].length) continue;
                    if (board[x+i][y+j] === 'E') updateBoard(board, [x+i, y+j]);
                }
        }
    }
    return board;
};
