/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort(function(n1, n2) {
        if (n1 < n2) return -1;
        if (n1 > n2) return 1;
        return 0;
    });
    var i, len = nums.length, avg = target / 3, belowIndex = -1;
    for (i = 0; i < len; i++) {
        if (nums[i] < avg) {
            belowIndex = i;
        } else {
            break;
        }
    }
    var diff = Number.MAX_SAFE_INTEGER, ans;
    var checkClosest = function(t) {
        var d = Math.abs(target - t);
        if (d < diff) {
            diff = d;
            ans = t;
        }
        return t >= target;
    };
    var twoSum = function(picked, head, tail) {
        while (head < tail) {
            if (checkClosest(picked + nums[head] + nums[tail])) {
                tail--;
            } else {
                head++;
            }
        }
    };
    if (len - belowIndex > 3) {
        checkClosest(nums[belowIndex + 1] + nums[belowIndex + 2] + nums[belowIndex + 3]);
    }
    if (belowIndex >= 2) {
        checkClosest(nums[belowIndex] + nums[belowIndex - 1] + nums[belowIndex - 2]);
    }
    for (i = 0; i <= belowIndex; i++) {
        twoSum(nums[i], belowIndex + 1, len - 1);
    }
    for (i = belowIndex + 1; i < len; i++) {
        twoSum(nums[i], 0, belowIndex);
    }
    return ans;
};