/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function(strs, m, n) {
    let record = [];
    for (let i = 0; i <= m; i++) {
        record[i] = [];
        for (let j = 0; j <= n; j++) {
            record[i][j] = 0;
        }
    }
    let max = 0;
    for (let s = 0; s < strs.length; s++) {
        let zeroCount = 0, oneCount = 0;
        for (let c = 0; c < strs[s].length; c++) {
            if (strs[s][c] === '0') zeroCount++;
            else oneCount++;
        }
        for (let i = m; i >= zeroCount; i--) {
            for (let j = n; j >= oneCount; j--) {
                if (record[i - zeroCount][j - oneCount] !== 0 || (i === zeroCount && j === oneCount)) {
                    record[i][j] = Math.max(record[i][j], record[i - zeroCount][j - oneCount] + 1);
                    max = Math.max(record[i][j], max);
                }
            }
        }
    }
    return max;
};