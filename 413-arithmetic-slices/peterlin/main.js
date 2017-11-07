/**
 * @param {number[]} A
 * @return {number}
 */
var numberOfArithmeticSlices = function(A) {
    let x = 0;
    for (let i=0, j; i<A.length; i+=j-1) {
        for (j=2; i+j<A.length && A[i+j]-A[i+j-1]===A[i+1]-A[i]; ++j);
        x += (j-2) * (j-1) / 2;
    }
    return x;
};
