/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if ('' === digits) {
        return [];
    }
    let ret = [];
    let translator = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'};
    let dfs = function(str, index) {
        if (index === digits.length) {
            ret.push(str);
            return ;
        }
        for (let i = 0; i < translator[digits[index]].length; i++) {
            dfs(str + translator[digits[index]][i], index + 1);
        }
    };
    dfs('', 0);
    return ret;
};