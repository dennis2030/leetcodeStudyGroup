/**
 * @param {number[]} nums
 * @return {number}
 */
var triangleNumber = function(nums) {
    var c = 0;
    nums.sort((a, b) => a-b);
    for (var i=2;i<nums.length;++i) {
        for (var j=i-1, k;j>0;--j) {
            for (k=j-1;k>=0 && nums[j]+nums[k]>nums[i];--k);
            c += j-k-1;
        }
    }
    return c;
};
