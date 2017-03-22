/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    function isNumber(s) {
        if (s.length > 3 || s.length < 1 || (s.length > 1 && s.charAt(0) === '0') || parseInt(s, 10) > 255) return false;
        return true;
    }
    function divide(str) {
        let arr = [];
        if (str.length > 6 || str.length < 2) {
            return arr;
        }
        for (let i = 1; i < str.length; i++) {
            let s1 = str.substr(0, i);
            let s2 = str.substr(i);
            if (isNumber(s1) && isNumber(s2)) {
                arr.push(s1 + '.' + s2);
            }
        }
        return arr;
    }
    let ans = [];
    for (let i = 2; i < s.length - 1; i++) {
        let pre = divide(s.substr(0, i));
        let post = divide(s.substr(i));
        if (pre.length === 0 || post.length === 0) {
            continue;
        }
        for (let j = 0; j < pre.length; j++) {
            for (let k = 0; k < post.length; k++) {
                ans.push(pre[j] + '.' + post[k]);
            }
        }
    }
    return ans;
};