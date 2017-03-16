/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var wiggleSort = function(nums) {
    var swap = function(a, b) {
        var temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    };
    var quickSelect = function(start, end, target) {
        var pivot = nums[start];
        var i = start + 1, j = end;
        while(i <= j) {
            if (nums[i] < pivot) {
                i++;
            } else if (nums[j] >= pivot) {
                j--;
            } else {
                swap(i, j);
                i++;
                j--;
            }
        }
        swap(start, j);
        if (j === target) return;
        if (j < target) return quickSelect(j + 1, end, target);
        if (j > target) return quickSelect(start, j - 1, target);
    };
    var mid = Math.floor((nums.length - 1) / 2);
    quickSelect(0, nums.length - 1, mid);
    swap(0, mid);
    var head = 1, tail = (nums.length % 2 === 0) ? nums.length - 2 : (nums.length - 1);
    while (head < tail) {
        swap(head, tail);
        head += 2;
        tail -= 2;
    }
    head = 1, tail = (nums.length % 2 === 0) ? (nums.length - 1) : (nums.length - 2);
    while (head < tail) {
        if (nums[tail] === nums[0]) {
            tail -= 2;
        } else if (nums[head] !== nums[0]) {
            head += 2;
        } else {
            swap(head, tail);
            tail -= 2;
            head += 2;
        }
    }
    head = 2, tail = (nums.length % 2 === 0) ? (nums.length - 2) : (nums.length - 1);
    while (head < tail) {
        if (nums[tail] !== nums[0]) {
            tail -= 2;
        } else if (nums[head] === nums[0]) {
            head += 2;
        } else {
            swap(head, tail);
            tail -= 2;
            head += 2;
        }
    }
};