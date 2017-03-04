/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    var candidate = [], count = [0, 0];
    var index, threashold = Math.floor(nums.length / 3);
    nums.forEach(function(n) {
        index = candidate.indexOf(n);
        if (index >= 0) {
            count[index]++;
            return;
        }
        index = count.indexOf(0);
        if (index >= 0) {
            candidate[index] = n;
            count[index]++;
            return;
        }
        count[0]--;
        count[1]--;
    });
    count = [0, 0];
    nums.forEach(function(n) {
        count[candidate.indexOf(n)]++;
    });
    return candidate.filter(function(c, i) {
        return count[i] > threashold;
    });
};