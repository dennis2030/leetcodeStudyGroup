/**
 * @param {string} start
 * @param {string} end
 * @param {string[]} bank
 * @return {number}
 */
var minMutation = function(start, end, bank) {
    var d = (a, b) => {
        var x = 0;
        for (var i=0;i<a.length;++i) {
            x += (a[i] === b[i] ? 0 : 1);
        }
        return x;
    };
    var q = [start], m = {};
    m[start] = 0;
    while (q.length > 0) {
        c = q.shift();
        for (var i=0;i<bank.length;++i) {
            if (!(bank[i] in m) && d(c, bank[i]) === 1) {
                m[bank[i]] = m[c]+1;
                q.push(bank[i]);
            }
        }
    }
    return end in m ? m[end] : -1;
};
