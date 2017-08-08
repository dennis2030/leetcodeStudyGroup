/**
 * @param {number} N
 * @return {number}
 */
var countArrangement = function(N) {
    var s = new Array(N+1).fill(0);
    var f = (n) => {
        if (n === 1) return 1;
        var m = 0;
        for (var i=N;i>0;--i) {
            if (s[i] > 0) continue;
            if (n%i === 0 || i%n === 0) {
                s[i] = n;
                m += f(n-1);
                s[i] = 0;
            }
        }
        return m;
    }
    return f(N);
};
