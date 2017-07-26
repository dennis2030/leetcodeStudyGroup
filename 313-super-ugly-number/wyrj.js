/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */
var nthSuperUglyNumber = function(n, primes) {
    let ugly = [1], len = primes.length;
    let indices = new Array(len).fill(0);
    while (n > ugly.length) {
        let min = Number.MAX_SAFE_INTEGER;
        for (let i = 0; i < len; i++) {
            min = Math.min(min, primes[i] * ugly[indices[i]]);
        }
        ugly.push(min);
        for (let i = 0; i < len; i++) {
            if (min === primes[i] * ugly[indices[i]]) indices[i]++;
        }
    }
    return ugly[n - 1];
};
