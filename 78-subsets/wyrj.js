/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    let subsets = [];
    let len = Math.pow(2, nums.length);
    for (let n = 0; n < len; n++) {
        let element = [];
        for (let i = 0; i < nums.length; i++) {
            if (n & (1 << i)) {
                element.push(nums[i]);
            }
        }
        subsets.push(element);
    }
    return subsets;
};