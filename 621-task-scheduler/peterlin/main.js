/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    const m = {}, p = {};
    tasks.forEach(t => {
        m[t] = m[t] ? m[t]+1 : 1;
        p[t] = 0;
    });
    
    var k, g = tasks.length;
    for (k = 0; g > 0; k++) {
        let b = null;
        for (const c in m) {
            if (p[c] > k || m[c] === 0) continue;
            if (b === null || m[b] < m[c]) b = c;
        };
        if (b !== null) {
            g--;
            m[b]--;
            p[b] = k+n+1;
        }
    }    
    return k;
};
