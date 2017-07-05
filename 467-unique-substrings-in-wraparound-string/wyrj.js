/**
 * @param {string} p
 * @return {number}
 */
var findSubstringInWraproundString = function(p) {
    function fillArray(a, index, n) {
        while (n > 0) {
            if (a[index] >= n) break;
            a[index] = n;
            n--;
            index = (index + 1) % 26;
        }
    }
    function toInt(index) {
        return p.charCodeAt(index) - 97;
    }
    let arr = new Array(26).fill(0), start = 0;
    for (let i = 0, len = p.length; i < len; i++) {
        if (i === len - 1 || toInt(i + 1) !== (toInt(i) + 1) % 26) {
            fillArray(arr, toInt(start), i - start + 1);
            start = i + 1;
        }
    }
    return arr.reduce((a, b) => a + b);
};
