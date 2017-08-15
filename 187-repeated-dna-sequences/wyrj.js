/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    let toNum = {A: 0, C: (1 << 18), G: (2 << 18), T: (3 << 18)};
    function toDnaString(number) {
        let toChar = ['A', 'C', 'G', 'T'];
        let str = '';
        for (let i = 0; i < 10; i++) {
            str += toChar[number & 3];
            number = number >> 2;
        }
        return str;
    }
    
    let n = 0;
    let hashMap = {};
    let ans = [];
    for (let i = 0; i < 9; i++) {
        n = (n >> 2) + toNum[s[i]];
    }
    for (let i = 9; i < s.length; i++) {
        n = (n >> 2) + toNum[s[i]];
        if (!hashMap.hasOwnProperty(n)) {
            hashMap[n] = false;
        } else if (hashMap[n] === false) {
            ans.push(n);
            hashMap[n] = true;
        }
    }
    return ans.map(toDnaString);
};
