/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
    let n = 0, max = 0, record = [0];
    for (let step = 1; step <= nums.length; step++) {
        n = (nums[step - 1] === 0) ? n - 1 : n + 1;
        if (record[n] === void 0) {
            record[n] = step;
        } else {
            max = Math.max(max, step - record[n]);
        }
    }
    return max;
};