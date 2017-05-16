/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    if (nums.length === 0) return [[]];
    var x = subsets(nums.slice(1));
    var y = [];
    x.forEach((s) => {
        var a = s.slice(0);
        a.push(nums[0]);
        y.push(s);
        y.push(a);
    });
    return y;
};
