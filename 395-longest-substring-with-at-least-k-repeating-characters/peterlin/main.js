/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function(s, k) {
    var d = s;
    [...new Set(s)].filter(x => s.split(x).length <= k).forEach(x => { d = d.replace(x, ","); });
    if (d === s) return s.length;
    return Math.max.apply(null, d.split(",").map(x => { return longestSubstring(x, k); }));
};
