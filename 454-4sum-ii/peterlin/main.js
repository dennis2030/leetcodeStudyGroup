/**
 * @param {number[]} A
 * @param {number[]} B
 * @param {number[]} C
 * @param {number[]} D
 * @return {number}
 */
var fourSumCount = function(A, B, C, D) {
    var ab = new Map(), cd = new Map();
    A.forEach(a => {
        B.forEach(b => {
            if(ab.has(a+b)) ab.set(a+b, ab.get(a+b)+1);
            else ab.set(a+b, 1);
        });
    });
    C.forEach(c => {
        D.forEach(d => {
            if(cd.has(c+d)) cd.set(c+d, cd.get(c+d)+1);
            else cd.set(c+d, 1);
        });
    });
    var s = 0;
    ab.forEach((v, k) => {
        if (cd.has(-k)) {
            s += v * cd.get(-k);
        }
    });
    return s;
};
