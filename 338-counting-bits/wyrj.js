/**
 * @param {number} num
 * @return {number[]}
 */
var countBits = function(num) {
    let bits = [0], delta = 1, n = num;
    while (n > 0) {
        let limit = Math.min(num + 1, delta << 1);
        for (let i = delta; i < limit; i++) {
            bits[i] = bits[i - delta] + 1;
        }
        n = n >> 1;
        delta = delta << 1;
    }
    return bits;
};