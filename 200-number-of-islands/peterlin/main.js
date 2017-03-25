/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    var go = (x,y) => {
        if (grid[x][y] === "0") return 0;
        grid[x][y] = "0";
        if (x > 0) go(x-1, y);
        if (y > 0) go(x, y-1);
        if (x+1 < grid.length) go(x+1, y);
        if (y+1 < grid[0].length) go(x, y+1);
        return 1;
    };
    
    var a = 0;
    for (var i=0;i<grid.length;++i)
        for (var j=0;j<grid[i].length;++j) {
            a += go(i,j);
        }
    return a;
};
