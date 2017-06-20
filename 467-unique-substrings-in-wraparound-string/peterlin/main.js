/**
 * @param {string} p
 * @return {number}
 */
var findSubstringInWraproundString = function(p) {
    var arr = Array(26).fill(0);
    var c = 0, ans = 0;
    for (var i=0;i<p.length;++i) {
        var k = p.charCodeAt(i) - "a".charCodeAt(0);
        if (c > 0 && (p.charCodeAt(i)-p.charCodeAt(i-1)+26)%26 != 1) {
            c = 0;
        }
        ++c;
        arr[k] = Math.max(arr[k], c);
    }
    arr.forEach((v) => { ans += v; });
    return ans;
};
