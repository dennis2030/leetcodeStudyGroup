/**
 * @param {number[]} A
 * @return {number}
 */
var numberOfArithmeticSlices = function(A) {
    let diff = [];
    for (let i = 1; i < A.length; i++) {
        diff.push(A[i] - A[i - 1]);
    }
    function calc(n) {
        if (n < 2) return 0;
        return n * (n - 1) / 2;
    }
    let index = 0;
    let num = 0;
    for (let i = 1; i < diff.length; i++) {
        if (diff[i] !== diff[index]) {
            num += calc(i - index);
            index = i;
        } else if (i === diff.length - 1) {
            num += calc(i - index + 1)
        }
    }
    return num;
};
