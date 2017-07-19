/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {;
    let sqr = [0, 1];
    let arr = [0], index = 1;
    for (let i = 1; i <= n; i++) {
        if (i === sqr[index]) {
            arr.push(1);
            index++;
            sqr.push(index * index);
            continue;
        }
        let min = i;
        for (let j = index - 1; j > 0; j--) {
            min = Math.min(min, arr[i - sqr[j]] + 1);
        }
        arr.push(min);
    }
    return arr[n];
};
