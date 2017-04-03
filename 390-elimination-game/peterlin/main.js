/**
 * @param {number} n
 * @return {number}
 */
var lastRemaining = function(n) {
    var f = (a) => {
        if (a === 1) return 1;
        return b(Math.floor(a/2))*2;
    };
    var b = (a) => {
        if (a === 1) return 1;
        return f(Math.floor(a/2))*2-1+a%2;
    };
    return f(n);
};
