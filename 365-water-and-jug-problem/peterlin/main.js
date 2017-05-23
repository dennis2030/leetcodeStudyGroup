/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {boolean}
 */
var canMeasureWater = function(x, y, z) {
    if (z === 0) return true;
    var gcd = (a, b) => {
        return a === 0 ? b : gcd(b%a, a); 
    };
    return z <= x+y && z%gcd(x, y) === 0;
};
