/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @param {string[][]} pairs
 * @return {boolean}
 */
var areSentencesSimilarTwo = function(words1, words2, pairs) {
    if (words1.length !== words2.length) return false;
    const m = new Map();
    pairs.forEach(p => {
        if (!m.has(p[0])) m.set(p[0], p[0]);
        if (!m.has(p[1])) m.set(p[1], p[1]);
        let p0 = m.get(p[0]), p1 = m.get(p[1]);
        while (p0 != m.get(p0)) p0 = m.get(p0);
        while (p1 != m.get(p1)) p1 = m.get(p1);
        m.set(p0, p1);
    });
    for (let i=0;i<words1.length;++i) {
        if (words1[i] === words2[i]) continue;
        if (!m.has(words1[i]) || !m.has(words2[i])) return false;
        let w1 = m.get(words1[i]), w2 = m.get(words2[i]);
        while (w1 != m.get(w1)) w1 = m.get(w1);
        while (w2 != m.get(w2)) w2 = m.get(w2);
        if (w1 !== w2) return false;
    }
    return true;
};
