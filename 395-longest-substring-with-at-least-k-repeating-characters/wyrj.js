/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function(s, k) {
    if (s.length < k) return 0;
    let arr = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        arr[s.charCodeAt(i) - 97] += 1;
    }
    let min = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== 0 && min > arr[i]) min = arr[i];
    }
    if (min >= k) return s.length;
    let r = '[';
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== 0 && arr[i] < k) r += String.fromCharCode(i + 97);
    }
    r += ']';
    let maxCount = 0;
    let splited = s.split(new RegExp(r)).filter((e) => e.length);
    for (let i = 0; i < splited.length; i++) {
        maxCount = Math.max(maxCount, longestSubstring(splited[i], k));
    }
    return maxCount;
};
