/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    var p, h = false, a = [];
    var s = "";
    for (var i=0;i<nums.length;++i) {
        if (i === 0 || nums[i]-1 !== nums[i-1]) {
            if (i > 0) {
                if (h) s += nums[i-1];
                a.push(s);
            }
            p = i;
            s = "" + nums[i];
            h = false;
        } else {
            if (i === p+1) {
                s += "->";
            }
            h = true;
        }
    }
    if (nums.length > 0) {
        if (h) s += nums[nums.length-1];
        a.push(s);
    }
    return a;
};
