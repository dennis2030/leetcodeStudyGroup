/**
 * @param {number[][]} wall
 * @return {number}
 */
var leastBricks = function(wall) {
    var m = new Map();
    wall.forEach(r => {
        var x = 0;
        r.forEach(b => {
            if (x > 0) m.set(x, m.has(x) ? m.get(x)+1 : 1);
            x += b;
        });
    });
    var a = wall.length;
    m.forEach((v, k) => {
        a = Math.min(a, wall.length-v);
    });
    return a;
};
