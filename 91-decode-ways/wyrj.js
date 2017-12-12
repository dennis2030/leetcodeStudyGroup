/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    if (s.length === 0) return 0;
    function check(str) {
        return str[0] !== '0' && parseInt(str, 10) <= 26;
    }
    let arr = [1];
    for (let i = 0; i < s.length; i++) {
        arr[i + 1] = 0;
        if (s[i] !== '0') {
            arr[i + 1] += arr[i];
        }
        if (i > 0 && check(s.substr(i - 1, 2))) {
            arr[i + 1] += arr[i - 1];
        }
        if (arr[i + 1] === 0) return 0;
    }
    return arr[s.length];
};
