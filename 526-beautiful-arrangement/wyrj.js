/**
 * @param {number} N
 * @return {number}
 */
var countArrangement = function(N) {
    let count = 0;
    let arr = new Array(N + 1).fill(0);
    function r(n) {
        if (n === 1) {
            count += 1;
            return;
        }
        for (let i = 1; i <= N; i++) {
            if (arr[i] === 0 && (n % i === 0 || i % n === 0)) {
                arr[i] = n;
                r(n - 1);
                arr[i] = 0;
            }
        }
    }
    r(N);
    return count;
};
