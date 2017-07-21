/**
 * @param {string} expression
 * @return {string}
 */
var fractionAddition = function(expression) {
    var gcd = (a, b) => {
        if (a<0) a=-a;
        if (b<0) b=-b;
        return b>0 ? gcd(b, a%b) : a;
    }
    var f = (expr, n, d) => {
        if (n === 0) d = 1;
        if (expr.length == 0) return ""+n+"/"+d;
        var res = expr.match(/([+|-]?\d+)\/(\d+)/);
        var cn = parseInt(res[1]);
        var cd = parseInt(res[2]);
        n = n*cd + d*cn;
        d *= cd;
        return f(expr.substring(res[0].length), n/gcd(n, d), d/gcd(n, d));
    }
    return f(expression, 0, 1);
};
