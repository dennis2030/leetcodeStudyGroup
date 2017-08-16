/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    let record = new Array(10).fill(0);
    let len = secret.length;
    let aCount = 0, bCount = len;
    for (let i = 0; i < len; i++) {
        if (secret[i] === guess[i]) {
            aCount += 1;
        } else {
            record[secret[i]] += 1;
            record[guess[i]] -= 1;
        }
    }
    bCount -= aCount;
    record.forEach((r) => {
        bCount -= Math.max(r, 0);
    });
    return '' + aCount + 'A' + bCount + 'B';
};
