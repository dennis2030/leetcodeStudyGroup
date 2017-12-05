/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    let map = {};
    function isReverse(str) {
        return str === str.split('').reverse().join('');
    }
    function r(str) {
        if (map[str]) return map[str];
        let ans = [];
        if (isReverse(str)) ans.push([str]);
        for (let i = 1; i < str.length; i++) {
            let sub = str.substr(0, i);
            if (!isReverse(sub)) continue;
            let subAns = r(str.substr(i));
            for (let j = 0; j < subAns.length; j++) {
                ans.push([sub].concat(subAns[j]));
            }
        }
        map[str] = ans;
        return ans;
    }
    return r(s);
};
