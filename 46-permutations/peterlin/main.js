/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    var p = [], d = {};
    var f = (q) => {
        if (q.length === nums.length) {
            p.push(q.slice());
            return;
        }
        for (var i=0; i<nums.length;++i) {
            if (i in d) continue;
            var a = q.slice();
            a.push(nums[i]);
            d[i] = true;
            f(a);
            delete d[i];
        }
    }
    f([]);
    return p;
};
