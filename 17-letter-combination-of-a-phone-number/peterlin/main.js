/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    let p = [" ","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"];
    var f = (d) => {
        if (d.length === 0) {
            return [""];
        }
        var b = [];
        var c = p[parseInt(d[0])];
        var v = f(d.substr(1));
        for (var i=0;i<c.length;++i) {
            for (var x in v) {
                b.push(c[i]+v[x]);
            }
        }
        return b;
    };
    return digits.length === 0 ? [] : f(digits);
};
