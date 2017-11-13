/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    const p = Array(s.length+1).fill(0);
    p[0] = 1;
    for (let i=0; i<s.length; ++i) {
        const n = parseInt(s[i]);
        if (n > 0) p[i+1] = p[i];
        const m = i > 0 ? parseInt(s.slice(i-1, i+1)) : 0;
        if (m >= 10 && m <= 26) p[i+1] += p[i-1];
    }
    return s ? p[s.length] : 0;
};
