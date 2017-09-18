/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    var result = [];
    var check = [];
    var recurrsive = function(arr, index) {
        if (index === nums.length) {
            result.push(arr.slice(0));
            return;
        }
        var i;
        for (i = 0; i < nums.length; i++) {
            if (check[i]) {
                continue;
            }
            check[i] = true;
            arr[index] = nums[i];
            recurrsive(arr, index + 1);
            check[i] = false;
        }
    }
    recurrsive([], 0);
    return result;
};
