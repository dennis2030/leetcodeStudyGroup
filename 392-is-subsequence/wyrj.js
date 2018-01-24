/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let si = 0;
    for (let ti = 0; ti < t.length && si < s.length; ti++) {
        if (s[si] === t[ti]) {
            si += 1;
        }
    }
    return si === s.length;
};
