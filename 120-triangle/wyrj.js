/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    for (let i = triangle.length - 2; i >= 0; i--) {
        let arr = triangle[i];
        for (let j = 0; j < arr.length; j++) {
            arr[j] += Math.min(triangle[i + 1][j], triangle[i + 1][j + 1]);
        }
    }
    return triangle[0][0];
};
