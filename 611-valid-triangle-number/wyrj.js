/**
 * @param {number[]} nums
 * @return {number}
 */
var triangleNumber = function(nums) {
    nums.sort((l, r) => l - r);
    const len = nums.length;
    function b(n) {
        let l = 0;
        let r = len;
        while (l < r) {
            let m = Math.ceil((l + r) / 2);
            let v = nums[m];
            if (v < n) l = m;
            else r = m - 1;
        }
        return r;
    }
    
    let count = 0;
    for (let i = 0; i < len - 2; i++) {
        for (let j = i + 1; j < len - 1; j++) {
            let k = b(nums[i] + nums[j]);
            count += Math.max(k - j, 0);
        }
    }
    return count;
};
