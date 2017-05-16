/**
 * @param {number} num
 * @return {number[]}
 */
var countBits = function(num) {
    var b = Array(num+1).fill(0);
    for (var i=1;i<=num;++i) b[i] += b[i&(i-1)] + 1;  
    return b;
};
