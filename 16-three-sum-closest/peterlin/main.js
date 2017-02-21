/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort( function(a, b){ return a-b; } );
    var ans = Infinity;
    for (var i=2;i<nums.length;++i) {
        var l = 0, r = i-1;
        while (l < r) {
            var val = nums[i] + nums[l] + nums[r];
            if (val === target) return target;
            if (Math.abs(ans-target) > Math.abs(val-target)) ans = val;
            if (val < target) ++l;
            else --r;
        }
    }
    return ans;
};
