/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    var a = [2, 3, 5];
    var b = [0, 0, 0];
    var c = [1];
    while (c.length < n) {
        var k = 0;
        for (var i=1;i<a.length;++i) {
            if (a[k]*c[b[k]] > a[i]*c[b[i]]) k = i;
        }
        var n2 = a[k]*c[b[k]];
        ++b[k];
        if (n2 === c[c.length-1]) continue;
        c.push(n2);
    }
    return c[c.length-1];
};
