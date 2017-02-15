/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    var a1 = version1.split('.');
    var a2 = version2.split('.');
    for (var i=0;i<a1.length || i<a2.length;++i) {
        var v1 = i<a1.length ? parseInt(a1[i]) : 0;
        var v2 = i<a2.length ? parseInt(a2[i]) : 0;
        if (v1 > v2) return 1;
        if (v1 < v2) return -1;
    }
    return 0;
};