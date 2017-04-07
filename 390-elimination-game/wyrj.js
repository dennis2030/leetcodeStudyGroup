/**
 * @param {number} n
 * @return {number}
 */
var lastRemaining = function(n) {
    let amount = n, delta = 1, force = false;
    while (amount > 1) {
        if (force || amount & 1) {
            n -= delta;
        }
        force = !force;
        delta = delta << 1;
        amount = amount >> 1;
    }
    return n;
};