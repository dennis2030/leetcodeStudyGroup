/**
 * @param {string} num
 * @return {boolean}
 */
var isAdditiveNumber = function(num) {
    function find(f, s, i) {
        if (i === num.length) return true;
        const next = f + s;
        const str = String(next);
        for (let si = 0; si < str.length; si++) {
            if (str[si] !== num[i + si]) return false;
        }
        return find(s, next, i + str.length)
    }
    const len = num.length;
    for (let i = 1; i < len / 2; i++) {
        const first = parseInt(num.substr(0, i), 10);
        for (let j = 1; j < len / 2; j++) {
            const second = parseInt(num.substr(i, j), 10);
            if (find(first, second, i + j)) {
                return true;
            }
            if (num[i] === '0') break;
        }
        if (num[0] === '0') return false;
    }
    return false;
};
