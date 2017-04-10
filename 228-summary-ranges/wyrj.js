/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    let summary = [], o = null;
    for (let i = 0; i < nums.length; i++) {
        if (!o || o.end !== nums[i] - 1) {
            o = {start:nums[i], end: nums[i]};
            summary.push(o);
        } else {
            o.end += 1;
        }
    }
    return summary.map((obj) => (obj.start === obj.end) ? ('' + obj.start) : ('' + obj.start + '->' + obj.end));
};