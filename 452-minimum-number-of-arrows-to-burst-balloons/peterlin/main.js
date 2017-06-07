/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    points.sort((a, b) => {
        if (a[0] === b[0]) return a[1] < b[1] ? -1 : 1;
        return a[0] < b[0] ? -1 : 1;
    });

    var a = 0, x = -Infinity;
    points.forEach((b) => {
        if (b[0] > x) {
            ++a;
            x = b[1];
            return;
        }
        if (b[1] < x) { x = b[1]; }
    });
    return a;
};
