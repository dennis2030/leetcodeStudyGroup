/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    var i, n1=Number.NaN, n2=Number.NaN, c1=0, c2=0;
    for (i=0;i<nums.length;++i) {
        if (n1 === nums[i]) { ++c1; continue; }
        if (n2 === nums[i]) { ++c2; continue; }

        if (c1 === 0) { n1 = nums[i]; c1 = 1; continue; }
        if (c2 === 0) { n2 = nums[i]; c2 = 1; continue; }
        --c1, --c2;
        if (c1 === 0) { n1 = Number.NaN; }
        if (c2 === 0) { n2 = Number.NaN; }
    }
    
    var ans = [];
    if (c1 > 0) {
        for (i=c1=0;i<nums.length;++i) c1 += (n1===nums[i]?1:0);
        if (c1*3 > nums.length) ans.push(n1);
    }
    if (c2 > 0) {
        for (i=c2=0;i<nums.length;++i) c2 += (n2===nums[i]?1:0);
        if (c2*3 > nums.length) ans.push(n2);
    }
    return ans;
};
