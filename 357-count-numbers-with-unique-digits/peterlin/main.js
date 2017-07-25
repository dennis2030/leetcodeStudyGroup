/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    if (n === 0) return 1;
    var a = 9;
    for (var i=1,j=9;i<n;++i,--j) a *= j;
    return countNumbersWithUniqueDigits(n-1) + a;
};
