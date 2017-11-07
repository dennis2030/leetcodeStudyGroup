/**
 * @param {number} num
 * @return {boolean}
 */
var isUgly = function(num) {
    [2, 3, 5].forEach(x => {
        for (; num > 0 && num % x === 0; num /= x);
    });
    return num === 1;
};
