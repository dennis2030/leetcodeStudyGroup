/**
 * @param {string} input
 * @return {number}
 */
var lengthLongestPath = function(input) {
    let max = 0, now = 0;
    let q = [];
    let r = /(?!\t)/;
    input.split('\n').forEach((s) => {
        let c = s.search(r);
        while (q.length > c) {
            now -= q.pop().length;
        }
        s = s.substr(c);
        now += s.length;
        q.push(s);
        if (s.indexOf('.') >= 0 && now + q.length - 1 > max) max = now + q.length - 1;
    });
    return max;
};
