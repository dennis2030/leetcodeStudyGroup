/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    var n = { 'A':0, 'C':1, 'G':2, 'T':3 };
    var h = 0;
    for (var i=0;i<10;++i) {
        h = h*4 + n[s[i]];
    }
    var o = {};
    var t = {};
    o[h] = true;
    for (var i=10;i<s.length;++i) {
        h = h*4 + n[s[i]] - n[s[i-10]]*Math.pow(4, 10);
        if (h in o) {
            t[h] = i-9;
        } else {
            o[h] = true;
        }
    }
    var x = [];
    for (var i in t) {
        x.push(s.substr(t[i], 10));
    }
    return x;
};
