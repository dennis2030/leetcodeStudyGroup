/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let rowCount = grid.length;
    let colCount = rowCount && grid[0].length;
    function flood(r, c) {
        if (r < 0 || r >= rowCount || c < 0 || c >= colCount || grid[r][c] === '0') return;
        grid[r][c] = '0';
        flood(r - 1, c);
        flood(r + 1, c);
        flood(r, c - 1);
        flood(r, c + 1);
    }
    let ans = 0;
    for (let i = 0; i < rowCount; i++) {
        for (let j = 0; j < colCount; j++) {
            if (grid[i][j] === '1') {
                ans++;
                flood(i, j);
            }
        }
    }
    return ans;
};