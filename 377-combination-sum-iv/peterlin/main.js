/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var combinationSum4 = function(nums, target) {
    var h = {};
    var f = (n) => {
        if (n < 0) return 0;
        if (n === 0) return 1;
        if (n in h) return h[n];
        h[n] = 0;
        for (var i in nums) h[n] += f(n - nums[i]);
        return h[n];
    }
    return f(target);
};
