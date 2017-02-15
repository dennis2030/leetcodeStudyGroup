/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    var st = 0, tank = 0;
    for (var i=0;i<gas.length*2;++i) {
        tank += gas[i%gas.length] - cost[i%gas.length];
        if (tank < 0) {
            st = i+1;
            tank = 0;
        }
    }
    return st<gas.length ? st : -1;
};