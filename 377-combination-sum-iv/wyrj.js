/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var combinationSum4 = function(nums, target) {
    let method = [];
    function fill(n) {
        if (method[n] !== void 0) return method[n];
        let m = 0;
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] < n) m += fill(n - nums[i]);
            else if (nums[i] === n) m += 1;
        }
        method[n] = m;
        return m;
    }
    return fill(target);
};