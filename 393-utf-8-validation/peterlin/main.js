/**
 * @param {number[]} data
 * @return {boolean}
 */
var validUtf8 = function(data) {
    var valid = true;
    while (data.length > 0 && valid) {
        var x = data.shift();
        if (x >> 7 === 0) continue;
        if (x >> 5 === 6 && data.length >= 1) {
            if (data.shift() >> 6 === 2) continue;
        } else if (x >> 4 === 14 && data.length >= 2) {
            if ((data.shift() >> 6 === 2) + (data.shift() >> 6 === 2) === 2) continue;
        } else if (x >> 3 === 30 && data.length >= 3) {
            if ((data.shift() >> 6 === 2) + (data.shift() >> 6 === 2) + (data.shift() >> 6 === 2) === 3) continue;
        }
        valid = false;
    }
    return valid;
};
