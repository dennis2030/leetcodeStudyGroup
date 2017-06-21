/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    points.sort((p1, p2) => {
        return (p1[0] !== p2[0]) ? (p1[0] - p2[0]) : (p1[1] - p2[1]);
    });
    let count = 0, limit = Number.MIN_SAFE_INTEGER;
    points.forEach((p) => {
        if (p[0] > limit) {
            count++;
            limit = p[1];
        } else if (p[1] < limit) {
            limit = p[1];
        }
    });
    return count;
};
