/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    var m = [...Array(s.length).keys()].map(i => Array(s.length).fill(false));
    for (let i=0; i<s.length; ++i) {
        m[i][i] = true;
        for (let j=1; j<=i && i+j<s.length && s[i+j]===s[i-j]; ++j) {
            m[i-j][i+j] = true;
        }
        for (let j=1; j<=i && i+j-1<s.length /*&& s[i+j-1]===s[i-j]*/; ++j) {
            if (s[i+j-1]!==s[i-j]) break;
            m[i-j][i+j-1] = true;
        }
    }
    const f = (c => {
        if (c.length === 0) {
            return [[]];
        }
        const offset = s.length - c.length;
        const p = [];
        for (let i=0; i<c.length; ++i) {
            if (!m[offset][offset+i]) continue;
            f(c.substring(i+1)).forEach(x => {
                p.push([c.substring(0, i+1)].concat(x));
            });
        }
        return p;
    });
    return f(s);
};
