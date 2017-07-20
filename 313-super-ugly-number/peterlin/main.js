/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */
var nthSuperUglyNumber = function(n, primes) {
    var s = [1];
    var pos = new Array(primes.length).fill(0);
    for (;n>1;--n) {
        var next = 0;
        for (var j=1;j<primes.length;++j) {
            if (s[pos[next]] * primes[next] > s[pos[j]] * primes[j]) {
                next = j;
            }
        }
        var cur = s[pos[next]] * primes[next];
        s.push(cur);
        for (var j=0;j<primes.length;++j) {
            if (cur === s[pos[j]] * primes[j]) {
                ++pos[j];
            }
        }
    }
    return s[s.length-1];
};
