/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    for (let i=0, j=0;i<t.length;++i) {
        if (s[j] == t[i]) ++j;
        if (j == s.length) return true;
    }
    return s.length == 0;
};
