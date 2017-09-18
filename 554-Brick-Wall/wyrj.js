/**
 * @param {number[][]} wall
 * @return {number}
 */
var leastBricks = function(wall) {
    let arr = [];
    for (let i = 0; i < wall.length; i++) {
        let sum = 0;
        for (let j = 0; j < wall[i].length - 1; j++) {
            sum += wall[i][j];
            arr.push(sum);
        }
    }
    arr.sort((l, r) => (l - r));
    let max = 0;
    for (let i = 0; i < arr.length; i++) {
        let v = arr[i];
        let count = 1;
        while (v === arr[i + 1]) {
            count +=1;
            i += 1;
        }
        max = Math.max(max, count);
    }
    return wall.length - max;
};
