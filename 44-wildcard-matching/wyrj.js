/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    var i, j;
    var prev = [], now = [true];
    for (j = 1; j <= s.length; j++) {
       now[j] = false;
    }
    for (i = 1; i <= p.length; i++) {
        prev = now;
        now = [('*' === p[i - 1] && prev[0])];
        for (j = 1; j <= s.length; j++) {
            if ('*' !== p[i-1]) {
                now[j] = (prev[j - 1] && (p[i - 1] === s[j - 1] || '?' === p[i - 1]));
            } else {
                now[j] = (prev[j] || now[j - 1]);
            }
        }
    }
    return now[s.length];
};