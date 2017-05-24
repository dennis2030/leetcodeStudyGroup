/**
 * @param {string} preorder
 * @return {boolean}
 */
var isValidSerialization = function(preorder) {
    var a = 1;
    var s = preorder.split(",");
    for (var i=0;i<s.length;++i) {
        if (a === 0) return false;
        if (s[i] === '#') --a;
        else ++a;
    }
    return a === 0;
};
