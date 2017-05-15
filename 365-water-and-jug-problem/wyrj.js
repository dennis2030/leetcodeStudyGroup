/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {boolean}
 */
var canMeasureWater = function(x, y, z) {
    function gcd(a, b) {
        return b === 0 ? a : gcd(b, a % b);
    }
    let d = gcd(x, y);
    return (z === 0 || (z <= x+y && z % d === 0));
};