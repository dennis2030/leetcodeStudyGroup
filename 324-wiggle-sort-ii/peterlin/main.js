/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var wiggleSort = function(nums) {
    var mid = Math.floor((nums.length-1)/2);
    var sw = (a,b) => { var x=nums[a]; nums[a]=nums[b]; nums[b]=x; };
    var qs = (st, ed) => {
        var x=nums[st],i=st+1,j=ed-1;
        if (ed-st <= 1) return x;
        while (i<=j){
            if (nums[i] <= x) ++i;
            else if(nums[j] > x) --j; 
            else sw(i++,j--);
        }
        sw(st, j);
        if (j === mid) return x;
        if (j > mid) return qs(st, j);
        return qs(j+1, ed);
    };
    qs(0, nums.length);

    mid = nums[mid];
    var pos = (a) => { return (2*a+1) % (nums.length|1); };    
    var i = 0, j = 0, k = nums.length - 1;
    while (j <= k) {
        if (nums[pos(j)] > mid)
            sw(pos(i++), pos(j++));
        else if (nums[pos(j)] < mid)
            sw(pos(j), pos(k--));
        else
            j++;
    }
};
