/**
 * @param {number[]} data
 * @return {boolean}
 */
var validUtf8 = function(data) {
    function leadOfOneZero(v) {
        return v !== void 0 && v >> 6 === 0b10;
    }
    function validator(idx) {
        if (idx >= data.length) return true;
        let n = data[idx];
        if (n >> 7 === 0) {
            return validator(idx + 1);
        } else if (n >> 5 === 0b110) {
            return leadOfOneZero(data[idx + 1]) && validator(idx + 2);
        } else if (n >> 4 === 0b1110) {
            return leadOfOneZero(data[idx + 1]) && leadOfOneZero(data[idx + 2]) && validator(idx + 3);
        } else if (n >> 3 === 0b11110) {
            return leadOfOneZero(data[idx + 1]) && leadOfOneZero(data[idx + 2]) && leadOfOneZero(data[idx + 3]) && validator(idx + 4);
        }
        return false;
    }
    
    return validator(0);
};
