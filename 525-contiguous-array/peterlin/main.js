/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
    var i, p = { 0:-1 }, a = 0;
    nums = nums.map((n) => { return n || -1; });
    for (i=1;i<nums.length;++i) nums[i]+=nums[i-1];
    for (i=0;i<nums.length;++i) {
        if (nums[i] in p) a=Math.max(a, i-p[nums[i]]);
        else p[nums[i]] = i;
    }
    return a;
};
