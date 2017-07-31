/**
 * @param {string} expression
 * @return {string}
 */

function gcd(a, b) {
    return b === 0 ? Math.abs(a) : gcd(b, a % b);
}
class Fraction {
    constructor(n, d) {
        this.n = n;
        this.d = d;
        this.reduce();
    }
    
    reduce() {
        let k = gcd(this.n, this.d);
        this.n = this.n / k;
        this.d = this.d / k;
    }
    
    add(f) {
        let k = gcd(this.d, f.d);
        this.n = this.n * (f.d / k) + f.n * (this.d / k);
        this.d = this.d / k * f.d;
        this.reduce();
    }
    
    toString() {
        return "" + this.n + "/" + this.d;
    }
}
var fractionAddition = function(expression) {
    let r = /^([+-]?\d+)\/(\d+)/;
    let ans = new Fraction(0, 1);
    while (expression.length > 0) {
        let m = expression.match(r);
        ans.add(new Fraction(parseInt(m[1], 10), parseInt(m[2], 10)));
        expression = expression.substr(m[0].length);
    }
    return ans.toString();
};
