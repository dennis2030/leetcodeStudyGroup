/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    var a = 1, b = nums.length-1;
    while (a <= b) {
        var mid = Math.floor((a+b)/2);
        if (nums.filter(x => x === mid).length > 1) return mid;
        nums.filter(x => x < mid).length >= mid ? b = mid-1 : a = mid+1;
    }
    return a;
};
