/**
 * @param {string} start
 * @param {string} end
 * @param {string[]} bank
 * @return {number}
 */
var minMutation = function(start, end, bank) {
    function dist(s1, s2) {
        let count = 0;
        for (let i = 0; i < s1.length; i++) {
            if (s1[i] !== s2[i]) count += 1;
        }
        return count;
    }

    let q = [start], q2 = [];
    let len = 0;
    while (q.length > 0) {
        q2 = q;
        q = [];
        for (let i = 0; i < q2.length; i++) {
            for (let j = bank.length - 1; j >= 0; j--) {
                if (dist(q2[i], bank[j]) === 1) {
                    if (bank[j] === end) {
                        return len + 1;
                    } else {
                        q.push(bank[j]);
                        bank[j] = bank[bank.length - 1];
                        bank.length -= 1;
                    }
                }
            }
        }
        len += 1;
    }
    return -1;
};
