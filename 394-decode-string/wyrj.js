/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    const ns = [], ss = [];
    let n = 0, str = '';
    for (let i = 0; i < s.length; i++) {
        if ('0' <= s[i] && s[i] <= '9') {
            n = n * 10 + parseInt(s[i], 10);
        } else if (s[i] === '[') {
            ns.push(n);
            ss.push(str);
            n = 0;
            str = '';
        } else if (s[i] === ']') {
            str = ss.pop() + str.repeat(ns.pop());
        } else {
            str += s[i];
        }
    }
    return str;
};
