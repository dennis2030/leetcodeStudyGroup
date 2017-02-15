/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    var s1 = version1.split('.');
    var s2 = version2.split('.');
    var i, len = Math.max(s1.length, s2.length), n1, n2;
    for (i = 0; i < len; i++) {
        n1 = (i < s1.length) ? parseInt(s1[i], 10) : 0;
        n2 = (i < s2.length) ? parseInt(s2[i], 10) : 0;
        if (n1 > n2) return 1;
        if (n1 < n2) return -1;
    }
    return 0;
};