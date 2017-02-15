/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    var delta, i;
    var total = 0, remain = 0, index = 0;
    for (i = 0; i < gas.length; i++) {
        delta = gas[i] - cost[i];
        total += delta;
        remain += delta;
        if (remain < 0) {
            index = i + 1;
            remain = 0;
        }
    }
    return (total < 0) ? -1 : index;
};